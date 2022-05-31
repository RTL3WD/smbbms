from django.shortcuts import redirect, render

from contacts.models import *
from contacts.forms import ContactPhoneNumberForm
# Create your views here.

def add_contact_phone(request, cid, pid):
    form = ContactPhoneNumberForm
    return redirect(f"contacts/contact/{cid}")