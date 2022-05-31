from django.forms import model_to_dict
from django.shortcuts import render

from contacts.models import *
from products.models import *
from transactions.models import *

def read_transaction(request,transaction_id):
    transaction_obj = Transaction.objects.get(id=transaction_id)
    transaction = model_to_dict(transaction_obj)
    contact_obj = Contact.objects.get(id=transaction['contact'])
    contact = model_to_dict(contact_obj)

    data = {
        "contact": contact,
        "transaction": transaction,
    }

    print(data)

    return render(request,"transactions/transaction.html",data)