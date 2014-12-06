from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView

from stats.forms import (GameUpdateForm, GamePlayedUpdateForm,
                            GoalInlineFormSet, GoalInlineFormSetHelper,
                                CardInlineFormSet, CardInlineFormSetHelper)
from stats.models import Season, Team, PlayFor, Matchday, Game, Goal, Card


def login_view(request):

    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.POST.get('next', '/'))
            else:
                context['invalid_alert'] = 'The account %s is inactive.'\
                    % username
        else:
            context['invalid_alert'] = 'Invalid username or password.'
            context['username'] = username
            context['next'] = request.POST.get('next', '/')
    else:
        context['next'] = request.GET.get('next', '/')

    return render(request, 'stats/login.html', context)


def logout_view(request):

    logout(request)
    context = { 'next': request.GET.get('next', '/') }

    return render(request, 'stats/logout.html', context)


@login_required(login_url='/login/')
def update_game_view(request, pk):

    game = get_object_or_404(Game, pk=pk)
    GoalFormSet = inlineformset_factory(
        Game,
        Goal,
        formset=GoalInlineFormSet,
        extra=1
    )
    CardFormSet = inlineformset_factory(
        Game,
        Card,
        formset=CardInlineFormSet,
        extra=1
    )

    if request.method == 'POST':
        form = GameUpdateForm(request.POST, instance=game)
        form_played = GamePlayedUpdateForm(request.POST, instance=game)
        home_goal_formset = GoalFormSet(request.POST,
            instance=game,
            prefix='home_goal'
        )
        away_goal_formset = GoalFormSet(request.POST,
            instance=game,
            prefix='away_goal'
        )
        card_formset = CardFormSet(request.POST, instance=game)
        if form.is_valid()\
            and form_played.is_valid()\
            and home_goal_formset.is_valid()\
            and away_goal_formset.is_valid()\
            and card_formset.is_valid():

            form.save()
            form_played.save()
            home_goal_formset.save()
            away_goal_formset.save()
            card_formset.save()
            return HttpResponseRedirect(game.get_absolute_url())

    else:
        form = GameUpdateForm(instance=game)
        form_played = GamePlayedUpdateForm(instance=game)
        home_goal_formset = GoalFormSet(
            prefix='home_goal',
            instance=game,
            queryset=Goal.objects.filter(
                scored_for=game.home_team,
            ).order_by('minute'),
            initial=[{
                'scored_for': game.home_team,
                'DELETE': True,
            }]
        )
        away_goal_formset = GoalFormSet(
            prefix='away_goal',
            instance=game,
            queryset=Goal.objects.filter(
                scored_for=game.away_team,
            ).order_by('minute'),
            initial=[{
                'scored_for': game.away_team,
                'DELETE': True,
            }]
        )
        card_formset = CardFormSet(
            instance = game,
            queryset = Card.objects.order_by('minute'),
            initial = [{
                'DELETE': True,
            }]
        )

    context = {
        'form': form,
        'form_played': form_played,
        'home_goal_formset': home_goal_formset,
        'away_goal_formset': away_goal_formset,
        'goal_formset_helper': GoalInlineFormSetHelper(),
        'card_formset': card_formset,
        'card_formset_helper': CardInlineFormSetHelper(),
        'game': game
    }

    return render(request, 'stats/game_update.html', context)


class TeamTemplateView(TemplateView):

    template_name = 'stats/team.html'

    def get_context_data(self, **kwargs):

        team = get_object_or_404(Team, slug=self.kwargs['team'])

        context = super(TeamTemplateView, self).get_context_data(**kwargs)
        context['team'] = team
        context['current_playfors'] = self.sort_playfors(
            team.get_current_playfors()
        )
        context['former_playfors'] = team.get_former_playfors()[:11]
        context['current_coachfors'] = self.sort_coachfors(
            team.get_current_coachfors()
        )
        context['seasons'] = Season.objects.filter(
            enrolled=team
        ).order_by('-end_date')

        return context


    # sort the list by injury reserve then positon then number
    # position G < D < M < F
    @staticmethod
    def sort_playfors(playfors):

        return sorted(playfors,
                key=lambda x:
                    ( x.injury_reserve, 0, x.number ) if x.player.position=='G'
                    else ( x.injury_reserve, 1, x.number ) if x.player.position=='D'
                    else ( x.injury_reserve, 2, x.number ) if x.player.position=='M'
                    else ( x.injury_reserve, 3, x.number ) if x.player.position=='F'
                    else ( x.injury_reserve, 4, x.number )
            )


    # sort the list by responsibility Coach < Assitant Coach < Manager
    @staticmethod
    def sort_coachfors(coachfors):

        return sorted(coachfors,
                key=lambda x:
                    0 if x.responsibility=='C'
                    else 1 if x.responsibility=='A'
                    else 2 if x.responsibility=='M'
                    else 3
            )


class MatchdayListView(ListView):

    model = Matchday
    context_object_name = 'matchday_list'
    template_name = 'stats/schedule.html'
    season = None

    def get_queryset(self, **kwargs):

        self.season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        return Matchday.objects.filter(
                season=self.season
            ).order_by('date').\
                prefetch_related('games__home_team',
                    'games__away_team', 'games__field')

    def get_context_data(self, **kwargs):

        context = super(MatchdayListView, self).get_context_data(**kwargs)
        context['season'] = self.season

        return context


class GameDetailView(DetailView):

    model = Game
    contex_object_name = 'game'
    template_name = 'stats/game.html'


class OverviewTemplateView(TemplateView):

    template_name = 'stats/overview.html'

    def get_context_data(self, **kwargs):

        season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        context = super(OverviewTemplateView, self).get_context_data(**kwargs)
        context['season'] = season
        context['standings'] = season.standings()
        context['matchdays'] = season.last_and_next_matchdays()
        context['scorers'] = season.with_teams(season.scorers())[:5]
        context['assistants'] = season.with_teams(season.assistants())[:5]

        return context


class StandingsTemplateView(TemplateView):

    template_name = 'stats/standings.html'

    def get_context_data(self, **kwargs):

        season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        context = super(StandingsTemplateView, self).get_context_data(**kwargs)
        context['season'] = season
        context['standings'] = season.standings()

        return context


class DisciplinaryListView(ListView):

    model = PlayFor
    context_object_name = 'playfor_list'
    template_name = 'stats/disciplinary.html'
    season = None

    def get_queryset(self, **kwargs):

        self.season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        return self.order_by_cards(
                self.season.booked_playfors(),
                self.season
            )

    def get_context_data(self, **kwargs):

        context = super(DisciplinaryListView, self).get_context_data(**kwargs)
        context['season'] = self.season

        return context

    @staticmethod
    def order_by_cards(playfors, season):

        for playfor in playfors:

            playfor.num_yellow_cards =\
                playfor.count_yellow_cards_per(season)
            playfor.num_red_cards =\
                playfor.count_red_cards_per(season)

        return sorted(
                playfors,
                key=lambda x: (x.num_red_cards, x.num_yellow_cards),
                reverse=True
            )

class GoalsListView(TemplateView):

    template_name = 'stats/goals.html'

    def get_context_data(self, **kwargs):

        season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        context = super(GoalsListView, self).get_context_data(**kwargs)
        context['season'] = season
        context['scorers'] = season.with_teams(season.scorers())
        context['assistants'] = season.with_teams(season.assistants())

        return context
