from django.shortcuts import render

from transactions.models import *

def index(request):
    transaction_objs = Transaction.objects.all()

    data = {
        "transactions": transaction_objs,
    }
    return render(request,"transactions/index.html",data)