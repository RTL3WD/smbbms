# import form class from django
from django import forms
from django.forms import DateInput, ModelForm, TextInput, EmailInput, Select, NumberInput, Textarea


# import GeeksModel from models.py
from products.models import Product

# create a ModelForm
class ProductForm(ModelForm):
	# specify the name of model to use
	class Meta:
		model = Product
		fields = "__all__"
		exclude = ('stripe_product_identifier','custom_fields','json')
		widgets = {
			'sku': TextInput(attrs={
				'class': 'form-control',
				'id': 'ContactType',
				'style': 'max-width: 100%;',
				'placeholder': 'Enter Stock Keeping Unit Identifier',
			}),
			'name': TextInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Product Name',
			}),
			'quantity': NumberInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Middle Name',
			}),
			'notes': Textarea(attrs={
				'class': 'form-control',
				'style': 'max-width: 100%;',
				'placeholder': 'Notes about the product',
			}),
		}
