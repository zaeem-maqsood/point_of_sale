from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MenuSerializer
from items.models import Item


class Menu(APIView):
    def get(self, request, *args, **kwargs):
        """
        Grab all the items with their modifier groups and related modifiers
        """

        items = Item.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
