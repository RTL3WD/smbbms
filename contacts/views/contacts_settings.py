from django.forms import model_to_dict
from django.http import HttpResponseBadRequest
from django.shortcuts import render

from contacts.models import *
# Create your views here.

def contacts_settings(request):
    return render(request,"contacts/widgets.html")
