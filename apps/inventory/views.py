from decimal import Decimal

from django.conf import settings
from django.db.utils import IntegrityError
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from .models import Product, Category, Subcategory
from .serializers import InventorySerializer


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


class InventoryAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request: Request, format=None):
        serializer = InventorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        category, _ = Category.objects.get_or_create(
            name=serializer.data['category'])
        subcategory, _ = Subcategory.objects.get_or_create(
            name=serializer.data['subcategory'], category_id=category.pk)

        try:
            Product(
                name=serializer.data.get('name'),
                description=serializer.data.get('description'),
                stock=serializer.data.get('stock'),
                price=Decimal(serializer.data['price']),
                image=request.data.get('image'),
                category_id=category.pk,
                subcategory_id=subcategory.pk
            ).save()
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)

        return Response(status=status.HTTP_200_OK)
