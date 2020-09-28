from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from students.models import CustomUser


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomUser.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!z")
            raise ValidationError("There is no user registered with the specified email address. Please mention "
                                  "your valid email.")

        return email