from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

from chat.models import Message


class UserSignUpForm(SignupForm):
    first_name = forms.CharField(label=_("First Name"),
                                 min_length=2,
                                 widget=forms.TextInput(
                                     attrs={'type': 'text',
                                            'placeholder': _('First name')})
                                 )
    last_name = forms.CharField(label=_("Last Name"),
                                min_length=2,
                                widget=forms.TextInput(
                                    attrs={'type': 'text',
                                           'placeholder': _('Last name')})
                                )


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}