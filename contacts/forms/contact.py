# import form class from django
from django import forms
from django.forms import DateInput, ModelForm, TextInput, EmailInput, Select

from contacts.models import Contact

from userdefinedfields.fields import ExtraFieldsJSONField


# create a ModelForm
class ContactForm(ModelForm):
	# specify the name of model to use
	class Meta:
		model = Contact
		fields = "__all__"
		extra_fields = ExtraFieldsJSONField(Contact)
		exclude = ('stripe_customer_identifier',)
		widgets = {
			'contact_type': Select(attrs={
				'class': 'form-control',
				'id': 'ContactType',
				'style': 'max-width: 100%;',
			}),
			'first_name': TextInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'First Name',
			}),
			'middle_name': TextInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Middle Name',
			}),
			'last_name': TextInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Last Name',
			}),
			'date_of_birth': DateInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Enter Date of Birth',
			}),
			'gender': Select(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Select Gender',
			}),
		}