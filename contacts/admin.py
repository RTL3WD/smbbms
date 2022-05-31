from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Contact, EmailAdmin, EmailAddress, PhoneAdmin, PhoneNumber, Address

from .resources import *

# Register your models here.

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # list_filter = ['name']
    list_display = ['id','first_name','last_name','contact_type']
    search_fields = ['first_name','last_name']
    resource_class = ContactResource

admin.site.register(Address)
admin.site.register(Contact, ContactAdmin)
admin.site.register(EmailAddress, EmailAdmin)
admin.site.register(PhoneNumber, PhoneAdmin)