from decimal import Decimal
from django.db import models


"""
Order model
has a payment_amount and note field

Method for adding line items also included
"""


class Order(models.Model):
    payment_amount = models.DecimalField(
        max_digits=6, decimal_places=2, default=Decimal(0.00)
    )
    note = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)

    def add_item(self, item, quantity):
        line_item = LineItem.objects.create(order=self, item=item, quantity=quantity)
        self.payment_amount += line_item.total
        self.save()
        return line_item.pk


"""
Line Item model

foreign keyed to an Order and an Item
quantity and line total also provided

save method overridden to update the total and decrement the item quantity
"""


class LineItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.00))

    def save(self, *args, **kwargs):
        self.total = self.item.price * self.quantity
        self.item.quantity -= self.quantity
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)
