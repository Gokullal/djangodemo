from django.contrib import admin

# Register your models here.

from cart.models import Cart
from cart.models import Payment
from cart.models import Order_details



admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Order_details)

