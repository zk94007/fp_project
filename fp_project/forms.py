from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import validate_email


User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def check_email(self, email):
        try:
            validate_email(email)
            return True
        except forms.ValidationError:
            return False

    def clean_email(self):
        if not self.check_email(self.cleaned_data['email']):
            raise forms.ValidationError("Please enter a valid email address")

        try:
            user = User.objects.get(email__exact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']

        raise forms.ValidationError('This email is already taken.', self.cleaned_data['email'])

