from django.contrib import admin
from .models import Order, LineItem


# Register your models here.
admin.site.register(Order)
admin.site.register(LineItem)
