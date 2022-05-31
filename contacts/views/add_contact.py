from contacts.forms import ContactForm

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

import stripe

# Create your views here.

def add_contact(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    context = {}     
    context['form'] = form
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'New Contact Created.')
    return redirect("contacts:index")