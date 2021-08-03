from django.urls import path
from .views import CreateOrder, Orders


urlpatterns = [
    path("", Orders.as_view()),
    path("create", CreateOrder.as_view()),
]
