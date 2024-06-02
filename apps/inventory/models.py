from django.db import models
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class ProductSubcategory(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=100, unique=True)
    category_id = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=100, unique=True)
    description = models.TextField(null=False, blank=False)
    quantity = models.IntegerField()
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
