from rest_framework import serializers 
from django.contrib.auth.models import User

#from restapp.models import Customer
from .models import Customer, Restaurant, Order, Payment, Feedback, City, FoodItem

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'orders')  

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email', 'address', 'pincode', 'password')
        

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id',
                  'name',
                  'phone', 
                  'email',
                  'password',
                  'pincode', 
                  'rating')   

            
class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ('id',
                  'customer',
                  'restaurant',
                  'fooditem',
                  'payment',
                  'order_status', 
                  'owner')                     

class PaymentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Payment
        fields = ('id',
                  'restaurant', 
                  'customer',
                  'payMode',
                  'payStatus',
                  'charges',
                  'owner')  

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id',
                  'order',
                  'restaurant', 
                  'customer',
                  'desc', 
                  'rating', 
                  'owner') 

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id',
                  'name')                   


class FoodItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = FoodItem
        fields = ('id',
                  'name',
                  'description',
                  'price', 
                  'image', 
                  'foodtype',
                  'is_available',
                  'owner')                      