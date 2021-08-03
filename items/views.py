from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
