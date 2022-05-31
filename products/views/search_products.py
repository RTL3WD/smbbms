from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse

from products.models import *
# Create your views here.

def search_products(request):
    if request.method == "POST":
        data = {}

        search_term = request.POST['search-products-input']
        data['searched'] = search_term

        try:
            search_term = int(search_term)
        except:
            pass

        if type(search_term) == int:

            sku_search = Product.objects.filter(sku__contains=search_term)
            data['sku_search'] = sku_search

        if type(search_term) == str:

            products = Product.objects.filter(name__contains=search_term)
            data['products'] = products

            sku_search = Product.objects.filter(sku__contains=search_term)
            data['sku_search'] = sku_search

        print(data)
        
        return render(request, "products/search-results.html", data)