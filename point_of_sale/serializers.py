from items.serializers import ItemSerializer
from modifiers.serializers import ModifierGroupSerializer


class MenuSerializer(ItemSerializer):
    modifier_groups = ModifierGroupSerializer(many=True, source="modifiergroup_set")
