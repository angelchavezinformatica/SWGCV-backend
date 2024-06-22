from decimal import Decimal, InvalidOperation

from rest_framework import serializers


class InventorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    stock = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    image = serializers.ImageField()
    category = serializers.CharField(max_length=100)
    subcategory = serializers.CharField(max_length=100)

    def validate_stock(self, value):
        try:
            value = int(value)
        except ValueError:
            raise serializers.ValidationError('Not is a number')

        return value

    def validate_price(self, value):
        try:
            value = Decimal(value)
        except InvalidOperation:
            raise serializers.ValidationError('Not is a valid decimal')

        return value
