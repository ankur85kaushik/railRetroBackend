from django.contrib import admin
from .models import Customer, Restaurant, Order, Payment, Feedback, City, FoodItem

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(City)
admin.site.register(FoodItem)