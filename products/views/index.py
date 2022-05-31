# Import product model/ form
# Render all instances of product model
# Allow submission of new product instance
# Also included is pagination
# For multiple pages of products

from django.core.paginator import Paginator
from django.shortcuts import render
from products.forms.product import ProductForm

from products.models import Product

# Create your views here.

def index(request):

    # Pagination
    products = Product.objects.all()
    pag = Paginator(products, 10)
    page = request.GET.get('page')
    products_page = pag.get_page(page)

    data = {
        "products": products,
        "products_page": products_page,
        "form": ProductForm(),
    }

    return render(request,"products/index.html",data)