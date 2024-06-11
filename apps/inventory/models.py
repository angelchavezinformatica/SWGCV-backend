import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone

from apps.account.models import User


class Category(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class Subcategory(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self) -> str:
        return self.name


class Sale(models.Model):
    datetime = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sales'
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)


class SaleDetail(models.Model):
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name='sale_details'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sale_details'
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super().save(*args, **kwargs)


@receiver(post_delete, sender=Product)
def delete_image(sender, instance: Product, **kwargs):
    image = str(instance.image)
    path_split = image.split('/')
    path = os.path.join(settings.BASE_DIR, 'media', *path_split)

    if os.path.isfile(path):
        os.remove(path)
