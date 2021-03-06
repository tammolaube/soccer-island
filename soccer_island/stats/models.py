import datetime

from django.db import models
from django.db.models import Count, Q, F, Prefetch
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify

class Classification(models.Model):

    label = models.CharField(
        max_length=32,
        unique=True,
        help_text='Please provide a label for the classification e.g.\
            \'Men\'s Open\'.'
    )
    slug = models.SlugField(
        max_length=32,
        unique=True
    )

    def __unicode__(self):

        return self.label

    def save(self, *args, **kwargs):

        self.slug = slugify(self.label)
        super(Classification, self).save(*args, **kwargs)


class Address(models.Model):

    street = models.CharField(max_length=128)
    city = models.CharField(max_length=64, default='Honolulu')
    state = models.CharField(max_length=2, default='HI')
    zip_code = models.CharField(max_length=16, default='968')
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):

        return self.street + ' ' + self.zip_code


class Suspension(models.Model):

    date_received = models.DateField(
        blank=True,
        null=True
    )
    suspended_until = models.DateField(
        blank=True,
        null=True
    )
    reason = models.CharField(
        max_length=1024,
        blank=True
    )
    fine = models.SmallIntegerField(help_text='Amount of US Dollar.')
    fine_paid = models.BooleanField(default=False)
    player = models.ForeignKey('Player')
    competition = models.ForeignKey(
        'Competition',
        blank=True,
        null=True
    )

    def __unicode__(self):

        return self.player.__unicode__() + ' ' + str(self.date_received)


class Person(models.Model):

    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(
        max_length=64,
        blank=True
    )
    last_name = models.CharField(max_length=64)
    birthday = models.DateField(
        blank=True,
        null=True
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
        blank=True
    )
    address = models.ForeignKey(
        Address,
        blank=True,
        null=True
    )

    def __unicode__(self):

        return self.first_name + ' ' + self.last_name


class Club(models.Model):

    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    address = models.ForeignKey(Address, blank=True, null=True)

    def __unicode__(self):

        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Club, self).save(*args, **kwargs)


class PlayFor(models.Model):

    player = models.ForeignKey('Player')
    team = models.ForeignKey('Team')
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(
        blank=True,
        null=True
    )
    injury_reserve = models.BooleanField(default=False)
    number = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex='^\d{1,2}$',
                message='Number must be between 0 and 99.'
            )
        ]
    )

    def count_yellow_cards_per(self, season):

        return Card.objects.filter(
            play_for=self,
            in_game__matchday__season=season,
            color='Y',
        ).count()

    def count_red_cards_per(self, season):

        return Card.objects.filter(
            play_for=self,
            in_game__matchday__season=season,
            color='R',
        ).count()

    def __unicode__(self):

        return self.player.__unicode__() + ' | ' + self.team.__unicode__()


class Team(models.Model):

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    colors = models.CharField(max_length=128)
    classification = models.ForeignKey(Classification)
    club = models.ForeignKey(Club, blank=True, null=True)

    def get_playfors(self):

        return PlayFor.objects.filter(
            team=self,
        )

    def get_current_playfors(self):

        return self.get_playfors().exclude(
            to_date__lt=datetime.date.today()
        )

    def get_former_playfors(self):

        return self.get_playfors().filter(
            to_date__lt=datetime.date.today()
        ).order_by(
            'to_date'
        )

    def get_current_coachfors(self):

        return CoachFor.objects.filter(
            team=self,
        ).exclude(
            to_date__lt=datetime.date.today()
        )

    def get_absolute_url(self):

        return reverse('team', args=(self.slug,))

    def __unicode__(self):

        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)


class Player(models.Model):

    person = models.OneToOneField(Person)
    registered = models.ManyToManyField(Team,
        through='PlayFor',
        through_fields=(
            'player',
            'team'
        )
    )
    POSITION_CHOICES = (
        ('', 'Allround'),
        ('F', 'Forward'),
        ('M', 'Midfield'),
        ('D', 'Defense'),
        ('G', 'Goal Keeper'),
    )
    position = models.CharField(
        blank=True,
        max_length=1,
        choices=POSITION_CHOICES,
        default=''
    )
    about = models.CharField(
        blank=True,
        max_length=1024,
        default = ''
    )

    def __unicode__(self):

        return self.person.__unicode__()

    def teams_per(self, season):

        return Team.objects.filter(
            season=season,
            playfor__player=self)

    def current_suspensions(self):

        return Suspension.objects.filter(
            player=self,
            suspended_until__gt=datetime.date.today,
            date_received__lt=datetime.date.today
        )



class Coach(models.Model):

    person = models.OneToOneField(Person)
    registered = models.ManyToManyField(
        Team,
        through='CoachFor',
        through_fields=(
            'coach',
            'team'
        )
    )

    def __unicode__(self):

        return self.person.__unicode__()


class CoachFor(models.Model):

    coach = models.ForeignKey(Coach)
    team = models.ForeignKey(Team)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    RESPONSIBILITY_CHOICES = (
            ('C', 'Coach'),
            ('M', 'Manager'),
            ('A', 'Assistant Coach'),
        )
    responsibility = models.CharField(
        max_length=1,
        choices=RESPONSIBILITY_CHOICES,
        null=False,
        default='C'
    )

    def __unicode__(self):

        return self.coach.__unicode__() + ' | ' + self.team.__unicode__()


class Referee(models.Model):

    person = models.OneToOneField(Person)

    def __unicode__(self):

        return self.person.__unicode__()


class Field(models.Model):

    name = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=64,
        unique=True
    )
    about = models.CharField(max_length=1024, blank=True)
    address = models.ForeignKey(Address)

    def __unicode__(self):

        return self.name

    def save(self, *args, **kwargs):

        self.slug = '%s-%s' % (slugify(self.name), slugify(self.address))
        super(Field, self).save(*args, **kwargs)


class Competition(models.Model):

    name = models.CharField(
        max_length=64
    )
    slug = models.SlugField(
        max_length=64
    )
    MODE_CHOICES = (
        ('L', 'League'),
        ('C', 'Cup'),
        ('R', 'Relegation'),
    )
    mode = models.CharField(
        max_length=1,
        choices=MODE_CHOICES
    )
    classification = models.ForeignKey(Classification)

    def __unicode__(self):

        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Competition, self).save(*args, **kwargs)


class Season(models.Model):

    label = models.CharField(
        max_length=9,
        help_text='Enter the label of the season in the format \'2014-2015\'.',
        validators=[
            RegexValidator(
                regex='^\d{4}-\d{4}$',
                message='Season label must be in the format \'YYYY-YYYY\'.'
            )
        ]
    )
    slug = models.SlugField(
        max_length=9
    )
    start_date = models.DateField()
    end_date = models.DateField()
    competition = models.ForeignKey(Competition)
    enrolled = models.ManyToManyField(Team)
    published = models.BooleanField(default=False)

    # This returns a Season or raises a 404 error.
    @staticmethod
    def get_season_by_slugs(classification, competition, season):

        print(season)

        if not season:

            return Season.get_current_season_by_slugs(classification, competition)

        """
        Slugs for classification, competition and season are
        unique. So we can use .get() instead of .filter().
        """
        season = get_object_or_404(
            Season.objects.select_related('competition__classification'),
            published=True,
            competition__slug=competition,
            competition__classification__slug=classification,
            slug=season
        )

        return season

    # This returns the current season
    @staticmethod
    def get_current_season_by_slugs(classification, competition):

        season = Season.objects.filter(
            published=True,
            competition__slug=competition,
            competition__classification__slug=classification,
        ).select_related(
            'competition__classification'
        ).order_by('-start_date')[:1][0]

        return season

    def get_teams(self):

        return Team.objects.filter(season=self)

    def standings(self):

        '''
        At the moment I get each teams home and away games.
        So I get each game, it's goals and who the goals where
        scored for twice.
        This can be improved but I'm not sure that the code will stay
        as readable.
        '''
        teams = Team.objects.filter(season=self)

        for team in teams:

            team.num_games = 0
            team.num_wins = 0
            team.num_draws = 0
            team.num_losses = 0
            team.num_scored_goals = 0
            team.num_conceded_goals = 0
            team.goal_diff = 0

            home_games = team.home.filter(
                matchday__season=self,
                played=True
            ).prefetch_related(
                Prefetch('goals__scored_for'),
            )

            away_games = team.away.filter(
                matchday__season=self,
                played=True
            ).prefetch_related(
                Prefetch('goals__scored_for'),
            )

            for game in list(home_games) + list(away_games):

                team.num_games += 1

                scored_goals = 0
                conceded_goals = 0

                for goal in game.goals.all():

                    if goal.scored_for == team:
                        scored_goals += 1
                    else:
                        conceded_goals += 1

                team.num_scored_goals += scored_goals
                team.num_conceded_goals += conceded_goals

                if scored_goals > conceded_goals:
                    team.num_wins += 1
                elif scored_goals == conceded_goals:
                    team.num_draws += 1
                else:
                    team.num_losses += 1

            team.num_points = team.num_draws + team.num_wins * 3
            team.goal_diff = team.num_scored_goals - team.num_conceded_goals

        return sorted(teams, key=lambda team:
            (team.num_points, team.goal_diff, team.num_scored_goals),
            reverse=True
        )

    def last_and_next_matchdays(self):

        last_matchday = Matchday.objects.filter(
            season=self,
            date__lt=(datetime.date.today())
        ).order_by('-date')[:1].\
            prefetch_related('games__home_team', 'games__away_team', 'games__field')

        next_matchday = Matchday.objects.filter(
            season=self,
            date__gte=(datetime.date.today())
        ).order_by('date')[:1].\
            prefetch_related('games__home_team', 'games__away_team', 'games__field')

        try:
            last_matchday = last_matchday[0]
        except IndexError:
            last_matchday = 'null'

        try:
            next_matchday = next_matchday[0]
        except IndexError:
            next_matchday = 'null'

        return (last_matchday, next_matchday,)

    def get_games_played(self):

        return Game.objects.filter(matchday__season=self).filter(played=True)

    def get_goals(self):

        return Goal.objects.filter(game__matchday__season=self)

    def count_goals(self):

        return self.get_goals().count()

    def scorers(self):

        return Player.objects.filter(
                playfor__goal_scored_by__game__matchday__season=self,
                playfor__goal_scored_by__scored_for=F('playfor__team')
            ).annotate(
                num_scored=Count('playfor__goal_scored_by')
            ).order_by(
                '-num_scored',
            )

    def assistants(self):

        return Player.objects.filter(
                playfor__goal_assisted_by__game__matchday__season=self,
            ).annotate(
                num_assisted=Count('playfor__goal_assisted_by'),
            ).order_by(
                '-num_assisted'
            )

    def with_teams(self, players):

        players = players.prefetch_related(
            Prefetch('registered',
                queryset=Team.objects.filter(season=self),
                to_attr='teams'
            )
        )

        return players

    def scorers_assistants(self):

        return Player.objects.filter(
                Q(playfor__goal_scored_by__game__matchday__season=self) |\
                Q(playfor__goal_assisted_by__game__matchday__season=self),
                playfor__goal_scored_by__own_goal=False,
            ).annotate(
                num_scored=Count('playfor__goal_scored_by'),
                num_assisted=Count('playfor__goal_assisted_by'),
            ).order_by(
                '-num_scored',
                '-num_assisted'
            )

    def booked_playfors(self):

        return PlayFor.objects.filter(
              card__in_game__matchday__season=self,
          ).annotate(
              num_of_cards=Count('card')
          )

    def yellow_booked_playfors(self):

        return PlayFor.objects.filter(
              card__in_game__matchday__season=self,
              card__color='Y'
          ).annotate(num_of_cards=Count('card'))

    def red_booked_playfors(self):

        return PlayFor.objects.filter(
              card__in_game__matchday__season=self,
              card__color='R'
          ).annotate(num_of_cards=Count('card'))

    def __unicode__(self):

        return '{1} {0}'.format(self.competition.__unicode__(), self.label)

    def get_absolute_url(self):

        return reverse('overview', kwargs={'classification':
            self.competition.classification.slug, 'competition':
            self.competition.slug, 'season': self.slug,})

    def get_schedule_url(self):

        return reverse('schedule', kwargs={'classification':
            self.competition.classification.slug, 'competition':
            self.competition.slug, 'season': self.slug,})

    def get_standings_url(self):

        return reverse('standings', kwargs={'classification':
            self.competition.classification.slug, 'competition':
            self.competition.slug, 'season': self.slug,})

    def get_goals_url(self):

        return reverse('goals', kwargs={'classification':
            self.competition.classification.slug, 'competition':
            self.competition.slug, 'season': self.slug,})

    def get_disciplinary_url(self):

        return reverse('disciplinary', kwargs={'classification':
            self.competition.classification.slug, 'competition':
            self.competition.slug, 'season': self.slug,})

    def save(self, *args, **kwargs):

        self.slug = slugify(self.label)
        super(Season, self).save(*args, **kwargs)


class Matchday(models.Model):

    label = models.CharField(
        max_length=32,
        help_text='Please provide a label. For examle: \'Matchday 1\', \
            \'Round of 16\', \'Playoffs: Final\''
    )
    slug = models.SlugField(max_length=32)
    season = models.ForeignKey(Season)
    date = models.DateField()

    def __unicode__(self):

        return self.label

    def save(self, *args, **kwargs):

        self.slug = slugify(self.label)
        super(Matchday, self).save(*args, **kwargs)


class Goal(models.Model):

    minute = models.SmallIntegerField(
        blank=True,
        validators=[
            RegexValidator(
                regex='^(\d{1,3})(\+\d{1,2})?$',
                message='Insert the minute the goal was scored. Specify stoppage times like \'45+2\' or \'90+3\'.'
            )
        ],
        max_length=6
    )
    scored_by = models.ForeignKey(
        PlayFor,
        related_name='goal_scored_by',
        blank=True,
        null=True
    )
    assisted_by = models.ForeignKey(
        PlayFor,
        related_name='goal_assisted_by',
        null=True,
        blank=True
    )
    scored_for = models.ForeignKey(Team, related_name='goal_scored_for')
    game = models.ForeignKey('Game', related_name='goals')

    def is_away(self):

        if self.scored_for == self.game.away_team:

            return True

        else:

            return False

    def __unicode__(self):

        return self.game.__unicode__() + ' ' + self.scored_for.__unicode__()


class Game(models.Model):

    date = models.DateTimeField()
    away_team = models.ForeignKey(
        Team,
        related_name='away',
        blank=True,
        null=True,
    )
    home_team = models.ForeignKey(
        Team,
        related_name='home',
        blank=True,
        null=True,
    )
    referee = models.ForeignKey(Referee, blank=True, null=True)
    field = models.ForeignKey(Field)
    matchday = models.ForeignKey(Matchday, related_name='games')
    played = models.BooleanField(
        default=False,
        help_text='Set this to true after the game has been played and all \
            data has been inserted. It will then be used for calculations of \
            standings.'
    )
    # for knock-out mode, see help_texts
    next_game = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        help_text='For knock-out mode only. To create a tree of teams \
            advancing.'
    )
    name = models.CharField(
        max_length=64,
        blank=True,
        help_text='For knock-out mode only (e.g. Semifinal A).'
    )

    def get_goals(self):

        return Goal.objects.filter(game=self).order_by('minute')

    def get_cards(self):

        return Card.objects.filter(in_game=self).order_by('minute')

    def get_home_goals(self):

        return Goal.objects.filter(game=self).filter(scored_for=self.home_team)

    def get_away_goals(self):

        return Goal.objects.filter(game=self).filter(scored_for=self.away_team)

    def get_score(self):

        if self.played:

            return '{0} - {1}'.format(
                self.get_home_goals().count(),
                self.get_away_goals().count()
            )

        else:

            return ' - '

    def get_winner(self):

        if self.get_home_goals().count() > self.get_away_goals().count():

            return self.home_team

        elif self.get_home_goals().count() < self.get_away_goals().count():

            return self.away_team

        else:

            return None

    def get_events(self):

        goals = self.get_goals().extra(select = {'event_type': 1})
        cards = self.get_cards().extra(select = {'event_type': 2})

        return sorted((list(goals) + list(cards)), key= lambda event:\
                event.minute)

    def __unicode__(self):

        return '{0} vs {1}'.format(
            self.home_team.__unicode__(),
            self.away_team.__unicode__(),
        )


    def get_absolute_update_url(self):

        return reverse('update_game', args=(self.pk,))


    def get_absolute_url(self):

        return reverse('game', args=(self.pk,))


class Card(models.Model):

    minute = models.SmallIntegerField(
        blank=True,
        validators=[
            RegexValidator(
                regex='^(\d{1,3})(\+\d{1,2})?$',
                message='Insert the minute the card was conceded. Specify stoppage times like \'45+2\' or \'90+3\'.'
            )
        ],
        max_length=6
    )
    COLOR_CHOICES = (
            ('Y', 'Yellow'),
            ('R', 'Red'),
        )
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, null=False)
    play_for = models.ForeignKey(PlayFor)
    in_game = models.ForeignKey(Game)

    def __unicode__(self):

        return '{0} Card ({1}min)'.format(
            self.color,
            str(self.minute)
        )
