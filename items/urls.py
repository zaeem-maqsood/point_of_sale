from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r"", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
