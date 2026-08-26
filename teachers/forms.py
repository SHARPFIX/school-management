from django import forms
from .models import teacher


INPUT_CLASS = (
    "w-full px-4 py-3 rounded-xl "
    "border border-slate-300 bg-white "
    "text-slate-900 "
    "placeholder-slate-400 "
    "shadow-sm "
    "outline-none "
    "transition-all duration-200 "
    "focus:border-indigo-500 "
    "focus:ring-4 focus:ring-indigo-500/10"
)


class TeacherForm(forms.ModelForm):

    class Meta:
        model = teacher

        fields = (
            "employee_id",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "qaulification",
            "specialization",
            "experience",
            "employement_type",
            "joining_date",
            "salary",
            "email",
            "phone_number",
            "photo",
            "is_class_teacher",
            "is_active",
        )

        widgets = {

            "employee_id": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Employee ID",
            }),

            "first_name": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Enter first name",
            }),

            "last_name": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Enter last name",
            }),

            "date_of_birth": forms.DateInput(attrs={
                "class": INPUT_CLASS,
                "type": "date",
            }),

            "gender": forms.Select(attrs={
                "class": INPUT_CLASS,
            }),

            "qaulification": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "e.g. B.Ed, M.Ed, M.Sc",
            }),

            "specialization": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "e.g. Mathematics",
            }),

            "experience": forms.NumberInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Years of experience",
                "min": "0",
            }),

            "employement_type": forms.Select(attrs={
                "class": INPUT_CLASS,
            }),

            "joining_date": forms.DateInput(attrs={
                "class": INPUT_CLASS,
                "type": "date",
            }),

            "salary": forms.NumberInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Monthly salary",
                "min": "0",
                "step": "0.01",
            }),

            "email": forms.EmailInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "teacher@example.com",
            }),

            "phone_number": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Phone number",
            }),

            "photo": forms.ClearableFileInput(attrs={
                "class": (
                    "w-full px-4 py-3 rounded-xl "
                    "border border-slate-300 "
                    "bg-white "
                    "text-slate-700 "
                    "file:mr-4 "
                    "file:py-2 "
                    "file:px-4 "
                    "file:rounded-lg "
                    "file:border-0 "
                    "file:bg-indigo-50 "
                    "file:text-indigo-700 "
                    "file:font-semibold "
                    "hover:file:bg-indigo-100"
                )
            }),

            "is_class_teacher": forms.CheckboxInput(attrs={
                "class": (
                    "w-5 h-5 rounded "
                    "border-slate-300 "
                    "text-indigo-600 "
                    "focus:ring-indigo-500"
                )
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": (
                    "w-5 h-5 rounded "
                    "border-slate-300 "
                    "text-indigo-600 "
                    "focus:ring-indigo-500"
                )
            }),
        }