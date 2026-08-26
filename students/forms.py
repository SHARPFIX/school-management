from django import forms
from .models import Student


INPUT_CLASS = (
    "w-full px-4 py-3 rounded-xl "
    "border border-slate-200 bg-white "
    "text-slate-900 placeholder-slate-400 "
    "outline-none transition duration-200 "
    "focus:border-indigo-500 "
    "focus:ring-4 focus:ring-indigo-500/10"
)


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = (
            "roll_number",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "email",
            "phone_number",
            "address",
            "city",
            "state",
            "father_name",
            "mother_name",
            "parent_phone",
            "photo",
            "is_active",
        )

        widgets = {

            "roll_number": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Roll number",
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "First name",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Last name",
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": INPUT_CLASS,
                    "type": "date",
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": INPUT_CLASS,
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "student@example.com",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Phone number",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Full address",
                    "rows": 3,
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "City",
                }
            ),

            "state": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "State",
                }
            ),

            "father_name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Father / Guardian name",
                }
            ),

            "mother_name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Mother name",
                }
            ),

            "parent_phone": forms.TextInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "Parent phone number",
                }
            ),

            "photo": forms.ClearableFileInput(
                attrs={
                    "class": (
                        "w-full px-4 py-3 rounded-xl "
                        "border border-slate-200 bg-white"
                    )
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": (
                        "w-5 h-5 rounded "
                        "text-indigo-600 "
                        "focus:ring-indigo-500"
                    )
                }
            ),
        }