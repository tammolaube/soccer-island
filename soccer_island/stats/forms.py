from django import forms

from stats.models import Goal, PlayFor, Game, Team
from django.db.models import Count, Q, F, Prefetch
from django.forms.models import inlineformset_factory, BaseInlineFormSet

class GameUpdateForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['date',
            'field', 'referee', 'played', 'matchday']


class GoalInlineFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(GoalInlineFormSet, self).__init__(*args, **kwargs)

        print(self.instance)

        for form in self.forms:

            form.fields['scored_by'].queryset = PlayFor.objects.\
                filter(
                    Q(team__home=self.instance) | Q(team__away=self.instance),
                    from_date__lte=self.instance.date,
                ).exclude(
                    to_date__lt=self.instance.date,
                ).select_related(
                    'player__person',
                    'team',
                )
            form.fields['assisted_by'].queryset = PlayFor.objects.\
                filter(
                    Q(team__home=self.instance) | Q(team__away=self.instance),
                    from_date__lte=self.instance.date,
                ).exclude(
                    to_date__lt=self.instance.date,
                ).select_related(
                    'player__person',
                    'team',
                )
            form.fields['scored_for'].queryset = Team.objects.filter(
                    Q(home=self.instance) | Q(away=self.instance),
                )
