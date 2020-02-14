from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

from application.models import User


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
    # photo = forms.ImageField(label=_("Profile Photo"),
    #                          widget=forms.FileInput(
    #                              attrs={'enctype': 'multipart/form-data'})
    #                          )
