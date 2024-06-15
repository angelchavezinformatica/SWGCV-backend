from django.db import models
from django.utils import timezone

from apps.inventory.models import Product


class Provider(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    phone_number = models.CharField(
        blank=False,
        null=False,
        max_length=9
    )


class Purchase(models.Model):
    datetime = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name='purchase_details'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='purchase_details'
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
