from django import forms
from django.forms import DateInput, ModelForm, TextInput, EmailInput, Select


from contacts.models import PhoneNumber

class ContactPhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ('phone_number','type')
        widgets = {
            'phone_number': TextInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 100%;',
            'placeholder': 'Phone Number',
			}),
			'type': Select(attrs={
            'class': 'form-control',
            'id': 'ContactType',
            'style': 'max-width: 100%;',
			}),
		}