from django.contrib import admin

from .models import (
    Product,
    Category,
    Sale,
    SaleDetail,
    Subcategory,
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.register(Subcategory)
