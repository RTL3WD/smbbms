from contacts.forms import ContactForm

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect,render

import stripe

# Create your views here.

def transactions_settings(request):
    return redirect("transactions:index")