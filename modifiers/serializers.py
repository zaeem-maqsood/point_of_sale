from rest_framework import serializers
from .models import ModifierGroup, Modifier

"""
Simple Model Serializer
"""


class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = "__all__"


"""
Simple Model Serializer
"""


class ModifierGroupSerializer(serializers.ModelSerializer):

    modifer = ModifierSerializer(many=True, source="modifier_set")

    class Meta:
        model = ModifierGroup
        fields = "__all__"
