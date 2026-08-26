from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


INPUT_CLASS = (
    "w-full px-4 py-3 rounded-xl "
    "border border-slate-200 bg-white "
    "text-slate-900 placeholder-slate-400 "
    "outline-none transition duration-200 "
    "focus:border-indigo-500 "
    "focus:ring-4 focus:ring-indigo-500/10"
)


class SchoolAdminRegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "First name",
        })
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "Last name",
        })
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "Choose a username",
            "autocomplete": "username",
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "you@example.com",
            "autocomplete": "email",
        })
    )

    phone_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "Phone number",
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "Create a password",
            "autocomplete": "new-password",
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": INPUT_CLASS,
            "placeholder": "Confirm your password",
            "autocomplete": "new-password",
        })
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = "school_admin"

        if commit:
            user.save()

        return user