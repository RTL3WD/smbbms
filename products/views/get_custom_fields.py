from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from products.models import *

def get_custom_fields(request):
    custom_fields = CustomField.objects.all()
    custom_field_values = CustomFieldValue.objects.all()

    print(custom_fields)
    print(custom_field_values)

    data = {
        "fields": custom_fields,
        "values": custom_field_values
    }

    print(data,sep="\n")

    return render(request, "products/custom-fields.html",data)