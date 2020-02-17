from allauth.account.forms import SetPasswordField, PasswordField
from django import forms
from django.utils.translation import gettext_lazy as _

from application.models import User


class UserSignUpForm(forms.models.ModelForm):
    email = forms.EmailField(label=_("Email Address"),
                             widget=forms.TextInput(
                                attrs={"type": "text",
                                       'placeholder': _('Email Address')}),
                             required=True)

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

    photo = forms.ImageField(label=_("Profile Photo"),
                             widget=forms.FileInput(
                                 attrs={
                                     'class': 'file-field input-field'
                                 }),
                             required=False)

    password1 = SetPasswordField(label='Password')
    password2 = PasswordField(label='Password (again)')

    class Meta:
        model = User
        exclude = ["is_active", "is_staff", "is_superuser", "password", "last_login", "groups", "user_permissions"]

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.photo = self.cleaned_data['photo']
        user.save()

        return user
