
# Import all contact models and contact form
# Include pagination for contact instances
from django.core.paginator import Paginator
from django.shortcuts import render

from contacts.models import *
from contacts.forms import ContactForm

# Create your views here.

def index(request):
    contact_objs = Contact.objects.all()
    contacts_list = list(contact_objs)
    for contact in contacts_list:
        if contact.contact_type == 'third_party':
            contact.contact_type = 'third party'

    # Setup Pagination
    pag = Paginator(contact_objs, 8)
    page = request.GET.get('page')
    contact_page = pag.get_page(page)

    context = {
        "contact_page": contact_page,
        "contact_form": ContactForm(),
    }

    return render(request, "contacts/app-contacts-list.html", context)