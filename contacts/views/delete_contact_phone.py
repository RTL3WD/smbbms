from re import template
from django.conf import settings
from django.forms import model_to_dict
from django.http import HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView

from contacts.models import *
# Create your views here.

def del_contact_phone(request, cid, pid):
    phone_number = PhoneNumber.objects.get(pk=pid)
    phone_number.delete()
    return redirect(f'/contacts/contact/{cid}')