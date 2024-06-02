import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class ProductSubcategory(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=100, unique=True)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=100, unique=True)
    description = models.TextField(null=False, blank=False)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(
        ProductSubcategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return self.name


class ProductHistory(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=False, blank=False)
    entry = models.BooleanField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='history')
    quantity = models.IntegerField()

    def __str__(self) -> str:
        entry = 'Entrada' if self.entry else 'Salida'
        return f"{self.product.name} - {str(self.quantity)} ({entry})"


@receiver(post_delete, sender=Product)
def delete_image(sender, instance: Product, **kwars):
    image = str(instance.image)
    path_split = image.split('/')
    path = os.path.join(settings.BASE_DIR, 'media', *path_split)

    if os.path.isfile(path):
        os.remove(path)
