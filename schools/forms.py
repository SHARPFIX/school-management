from django import forms
from .models import School


INPUT_CLASS = (
    "w-full px-4 py-3 rounded-xl "
    "border border-slate-200 bg-white "
    "text-slate-900 placeholder-slate-400 "
    "outline-none transition duration-200 "
    "focus:border-indigo-500 "
    "focus:ring-4 focus:ring-indigo-500/10"
)


class SchoolRegistrationForm(forms.ModelForm):

    class Meta:
        model = School

        fields = (
            "school_name",
            "school_code",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "principal_name",
            "established_year",
            "logo",
            "website",
        )

        widgets = {
            "school_name": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Enter school name",
            }),

            "school_code": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "e.g. SCH001",
            }),

            "email": forms.EmailInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "school@example.com",
            }),

            "phone": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "School phone number",
            }),

            "address": forms.Textarea(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Complete school address",
                "rows": 3,
            }),

            "city": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "City",
            }),

            "state": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "State",
            }),

            "country": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Country",
            }),

            "postal_code": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Postal code",
            }),

            "principal_name": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Principal name",
            }),

            "established_year": forms.NumberInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "e.g. 2005",
            }),

            "logo": forms.ClearableFileInput(attrs={
                "class": "w-full px-4 py-3 rounded-xl border border-slate-200 bg-white text-slate-600"
            }),

            "website": forms.URLInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "https://example.com",
            }),
        }