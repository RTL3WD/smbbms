from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from products.forms import ProductForm

import stripe

# Create your views here.

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'New Product created.')
    return redirect("products:index")