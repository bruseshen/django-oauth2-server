from django import forms

from apps.web import SCOPE_CHOICES


class AuthorizeForm(forms.Form):

    authorize = forms.BooleanField()
    scopes = forms.MultipleChoiceField(
        choices=SCOPE_CHOICES, widget=forms.CheckboxSelectMultiple)