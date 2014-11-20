from django import forms

from stats.models import Goal, PlayFor, Game, Team
from django.db.models import Count, Q, F, Prefetch
from django.forms.models import inlineformset_factory, BaseInlineFormSet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Div, HTML
from crispy_forms.bootstrap import InlineCheckboxes, StrictButton

class GameUpdateForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['date', 'field', 'referee',]

    def __init__(self, *args, **kwargs):
        super(GameUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class GamePlayedUpdateForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['played',]

    def __init__(self, *args, **kwargs):
        super(GamePlayedUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class GoalInlineFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GoalInlineFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.layout = Layout(
            Div(
                'game',
                Field('id', type="hidden", css_class="element-id"),
                Field('scored_for', type="hidden"),
                ## Div(
                    ## HTML('<strong class="text-muted">Goal #<span class="counter">{{ forloop.counter }}</span></strong>'),
                    ## css_class='panel-heading'
                ## ),
                Div(
                    Div(
                        Div(
                            Field('scored_by', css_class='input-sm'),
                            css_class='col-md-5'
                        ),
                        Div(
                            Field('assisted_by', css_class='input-sm'),
                            css_class='col-md-5'
                        ),
                        Div(
                            Field('minute', css_class='input-sm'),
                            css_class='col-md-2'
                        ),
                        css_class='row'
                    ),
                    css_class='panel-body'
                ),
                Div(
                    Div(
                        Field('DELETE'),
                        css_class='list-group-item'
                    ),
                    css_class='list-group delete-checkbox'
                ),
                css_class='panel panel-default'
            )
        )
        self.render_required_fields = False


class GoalInlineFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(GoalInlineFormSet, self).__init__(*args, **kwargs)

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
                ).distinct()
            form.fields['assisted_by'].queryset = PlayFor.objects.\
                filter(
                    Q(team__home=self.instance) | Q(team__away=self.instance),
                    from_date__lte=self.instance.date,
                ).exclude(
                    to_date__lt=self.instance.date,
                ).select_related(
                    'player__person',
                    'team',
                ).distinct()
