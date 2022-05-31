from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

from products.forms import ProductForm

import stripe

# Create your views here.

def app_settings(request):
    return render(request, "products/app-settings.html",)