from django.contrib import admin

from .models import (
    Product,
    ProductCategory,
    ProductHistory,
    ProductSubcategory,
)

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductHistory)
admin.site.register(ProductSubcategory)
