from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


"""
Modifier Group Model lined to the item model
"""


class ModifierGroup(models.Model):
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


"""
Modifier Model linked to the modifier group
"""


class Modifier(models.Model):

    group = models.ForeignKey("ModifierGroup", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=0.0, message="Cannot have a negative Price")
        ],
        default=Decimal(0.00),
    )

    def __str__(self):
        return self.name
