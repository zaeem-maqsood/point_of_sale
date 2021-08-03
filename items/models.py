from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
"""
Item Model: contains description, price and quantity
Basic validation added at a model level
"""


class Item(models.Model):
    description = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=0.0, message="Cannot have a negative Price")
        ],
        default=Decimal(0.00),
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.description
