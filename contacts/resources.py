from import_export import resources
from contacts.models import Contact

class ContactResource(resources.ModelResource):

    class Meta:
        model = Contact
        exclude = ('middle_name','date_of_birth','gender','stripe_customer_identifier')
        # export_order = ('',)
        # fields = ('',)