from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse

from contacts.models import *
# Create your views here.

def search_contacts(request):
    if request.method == "POST":

        data = {}

        search_term = request.POST['search-contacts-input']
        data['searched'] = search_term

        try:
            search_term = int(search_term)
        except:
            pass

        if type(search_term) == int:

            phone_number_contact = PhoneNumber.objects.filter(contact__first_name__icontains=search_term)
            data['contacts_with_phone_number'] = phone_number_contact

            phone_numbers = PhoneNumber.objects.filter(phone_number__contains=search_term)
            data['phone_numbers'] = phone_numbers

        if type(search_term) == str:
            contacts_first_names = Contact.objects.filter(first_name__contains=search_term)
            data['contacts'] = contacts_first_names
        
        return render(request, "contacts/search-results.html", data)
    else:
        return render(request, "contacts/search-results.html")
