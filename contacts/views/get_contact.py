from re import template
from django.conf import settings
from django.forms import model_to_dict
from django.http import HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView

from contacts.models import *
from userdefinedfields.models import ExtraField

# Create your views here.

class GetContactDetailView(DetailView):

    model = Contact

    template_name = "contacts/contact-profile.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the phone numbers
        context['phone_numbers'] = PhoneNumber.objects.filter(contact=context['contact'])
        context['emails'] = EmailAddress.objects.filter(contact=context['contact'])
        context['addresses'] = Address.objects.filter(contact=context['contact'])
        context['custom_field'] = ExtraField.objects.all()
        return context

@csrf_exempt
def stripe_config(request,id):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request,id):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})