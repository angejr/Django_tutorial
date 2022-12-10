from django.contrib import admin

# Register your models here.

from .models import Product
# Equivalent to : 
# from products.models import Product


# Add the product model to the admin page 
admin.site.register(Product)