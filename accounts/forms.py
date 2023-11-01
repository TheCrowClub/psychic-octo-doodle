from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


from accounts import models


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    first_name = forms.CharField(
        label="First Name",
        help_text=("Enter your first name"),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=("Enter the same password as before, for verification."),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput,
        help_text=("Enter your email. This will be used to verify you."),
    )

    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "username", "email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ChangeProfile(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "email"]
