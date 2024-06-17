from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Product, Category, Subcategory


def get_products():
    return [{
        'name': product.name,
        'description': product.description,
        'quantity': product.quantity,
        'price': product.price,
        'image': f"{settings.SERVER}media/{product.image.name}",
        'category': product.category.name,
        'subcategory': product.subcategory.name,
    } for product in Product.objects.all()]


def get_categories():
    return [{
        'category': category.name,
        'subcategories': [str(subcategory)
            for subcategory in Subcategory.objects.filter(
                category=category.id)]
    } for category in Category.objects.all()]


class InventoryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, format=None):
        products = get_products()
        categories = get_categories()

        return Response(data={
            'products': products,
            'categories': categories,
        })
