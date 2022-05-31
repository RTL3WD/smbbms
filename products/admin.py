from django.contrib import admin

from .models import *

# admin.site.register(CustomFieldValue)
# admin.site.register(Image, ImageAdmin)
# admin.site.register(Location)
admin.site.register(Price,PriceAdmin)
admin.site.register(Product)
# admin.site.register(ProductStorageLocation)
# admin.site.register(StorageLocation)