from django.contrib import admin
from .models import InvoiceItem, Transaction

# Register your models here.

admin.site.register(InvoiceItem)
admin.site.register(Transaction)