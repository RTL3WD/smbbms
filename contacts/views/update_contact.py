from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse

from contacts.models import *
# Create your views here.

def update_contact(request,id):
    return HttpResponse('UPDATE CONTACT FUNCTION')