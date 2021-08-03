from rest_framework import serializers
from .models import Item

"""
Simple Item Model Serializer 
"""


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
