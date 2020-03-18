from allauth.account.adapter import get_adapter
from allauth.account import app_settings
from allauth.account.forms import PasswordField
from allauth.account.utils import user_username, user_email, setup_user_email
from allauth.utils import set_form_field_order
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import LoginForm, BaseSignupForm

from application.models import User


class UserSignUpForm(BaseSignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(label=_("First Name"),
                                                    min_length=2,
                                                    widget=forms.TextInput(
                                                        attrs={'type': 'text',
                                                               'placeholder': _('First name')})
                                                    )
        self.fields['last_name'] = forms.CharField(label=_("Last Name"),
                                                   min_length=2,
                                                   widget=forms.TextInput(
                                                       attrs={'type': 'text',
                                                              'placeholder': _('Last name')})
                                                   )

        self.fields['photo'] = forms.ImageField(label=_("Profile Photo"),
                                                widget=forms.FileInput(
                                                    attrs={
                                                        'class': 'file-field input-field'
                                                    }),
                                                required=False)
        self.fields['password1'] = PasswordField(label=_("Password"))
        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields['password2'] = PasswordField(
                label=_("Password (again)"))

        if hasattr(self, 'field_order'):
            set_form_field_order(self, self.field_order)

    def clean(self):
        super(UserSignUpForm, self).clean()

        # `password` cannot be of type `SetPasswordField`, as we don't
        # have a `User` yet. So, let's populate a dummy user to be used
        # for password validaton.
        dummy_user = get_user_model()
        user_username(dummy_user, self.cleaned_data.get("username"))
        user_email(dummy_user, self.cleaned_data.get("email"))
        password = self.cleaned_data.get('password1')
        if password:
            try:
                get_adapter().clean_password(
                    password,
                    user=dummy_user)
            except forms.ValidationError as e:
                self.add_error('password1', e)

        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE \
                and "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                self.add_error(
                    'password2',
                    _("You must type the same password each time."))
        return self.cleaned_data

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # TODO: Move into adapter `save_user` ?
        setup_user_email(request, user, [])
        return user
