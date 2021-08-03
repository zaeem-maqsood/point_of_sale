from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CreateOrderSerializer, OrderSerializer
from .models import Order


class CreateOrder(APIView):
    def post(self, request, *args, **kwargs):
        """
        Post method checks that the order exists and adds the item and quantity
        if those values pass validation
        """

        print(request.data)
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order = serializer.save()
            return Response({"orderID": order.id})


class Orders(APIView):
    def get(self, request, *args, **kwargs):
        """
        Grab all the orders with their line items
        """

        orders = Order.objects.all()
        print(orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
