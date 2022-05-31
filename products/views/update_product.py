from products.forms import ProductForm
from products.models import Product

from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http.response import JsonResponse 
from django.shortcuts import render, redirect
from django.template import context
from django.views.decorators.csrf import csrf_exempt

import stripe

# Create your views here.

def update_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product = model_to_dict(product)
    print(product)
    return render(request,"products/edit-product.html", product)

