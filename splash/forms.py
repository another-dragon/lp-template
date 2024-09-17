from django import forms
from .models import User
import logging

logger = logging.getLogger(__name__)

class UserForm(forms.ModelForm):
    marketing_consent = forms.BooleanField(
        required=False,
        label='Do you want to hear from us about our other properties?',
        widget=forms.CheckboxInput(attrs={'class': 'focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'marketing_consent']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        logger.info(f"Cleaning first_name: {first_name}")
        if not first_name.isalpha():
            logger.error(f"Invalid first_name: {first_name}", exc_info=True)
            raise forms.ValidationError("First name should contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        logger.info(f"Cleaning last_name: {last_name}")
        if not last_name.isalpha():
            logger.error(f"Invalid last_name: {last_name}", exc_info=True)
            raise forms.ValidationError("Last name should contain only letters.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        logger.info(f"Cleaning email: {email}")
        # Implement any future email validation logic here
        return email