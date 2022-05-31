from django.test import TestCase
from products.models import Product
import datetime

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        start_time = datetime.datetime.now()
        products = []
        batch_size = 500
        for i in range(1000000):
            product = Product()
            product.sku = "SKU: " + str(i)
            product.name = "Name: " + str(i)
            product.quantity = 1
            products.append(product)
        Product.objects.bulk_create(products, batch_size)

        end_time = datetime.datetime.now()
        print(f" Created in {end_time - start_time}")

    def test_lookup(self):
        start_time = datetime.datetime.now()
        for i in range(50000, 51000):
            # Product.objects.get(sku=f"SKU: {i}")
            Product.objects.filter(name=f"Name: {i}").get(sku=f"SKU: {i}")

        end_time = datetime.datetime.now()
        print(f"Looked up in {end_time - start_time}")