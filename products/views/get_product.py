from django.forms import model_to_dict
from django.shortcuts import render

from products.models import Product

# Create your views here.

def merge(dict1, dict2):
    return(dict2.update(dict1))


def get_product(request,product_id):

    product = Product.objects.get(pk=product_id)
    product = model_to_dict(product)

    final_product = product.copy()

    final_product = final_product.update(product)
    
    print(final_product)
    
   

    return render(request,"products/product.html",product)