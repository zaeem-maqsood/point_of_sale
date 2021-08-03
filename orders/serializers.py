from collections import Counter
from rest_framework import serializers
from .models import Order, LineItem
from items.models import Item
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator


"""
Serialize the item id and quantity from the data we get
"""


class LineItemSerializer(serializers.Serializer):

    item = serializers.IntegerField(
        validators=[MinValueValidator(limit_value=0, message="ID must be positive")]
    )
    quantity = serializers.IntegerField(
        validators=[
            MinValueValidator(limit_value=0, message="Quantity must be positive")
        ]
    )


"""
Serialize the Line Items and note we get on the order creation

validate the quantities 

Save each Line item to the order if validation succeeds
"""


class CreateOrderSerializer(serializers.Serializer):
    line_items = LineItemSerializer(many=True)
    note = serializers.CharField(max_length=200, required=False, allow_blank=True)

    def validate(self, data):

        # Create a counter to track all item instances
        # In case we are passed the same item on different lines
        # Should probably make sure this doesn't happen from the
        # Frontend but we'll check it here regardless
        counter = Counter()

        for line_item in data["line_items"]:
            line_item = list(line_item.items())
            item_id = line_item[0][1]
            quantity = line_item[1][1]
            counter[f"{item_id}"] += quantity

        # Loop through the items to make sure the quantities are good
        for key, value in counter.items():
            try:
                item = Item.objects.get(id=key)
                if value > item.quantity:
                    raise serializers.ValidationError(
                        f"There are only {item.quantity} items available for item {key} you asked for {value}"
                    )
            except ObjectDoesNotExist:
                raise serializers.ValidationError(f"There is no Item with ID of {key}")

        return data

    # Finally after validation is passed
    # Create the order object and add the line items
    def create(self, validated_data):

        order = Order.objects.create(note=validated_data["note"])
        line_items = validated_data["line_items"]
        for line_item in line_items:
            line_item = list(line_item.items())
            item_id = line_item[0][1]
            quantity = line_item[1][1]
            item = Item.objects.get(id=item_id)
            order.add_item(item, quantity)

        return order


"""
Simple model serializer for listing orders
"""


class LineItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ["item", "quantity", "total"]


class OrderSerializer(serializers.ModelSerializer):
    line_items = LineItemModelSerializer(many=True, source="lineitem_set")

    class Meta:
        model = Order
        fields = "__all__"
