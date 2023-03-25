from django.contrib import admin
from .models import ShippingAddress , Product , Customer , Order ,OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

