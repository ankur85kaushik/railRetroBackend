from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework import permissions
from restapp.permissions import IsOwnerOrReadOnly

from rest_framework import viewsets

from restapp.models import Customer
from restapp.serializers import CustomerSerializer    
from restapp.models import City
from restapp.serializers import CitySerializer

from restapp.models import Restaurant
from restapp.serializers import RestaurantSerializer

from restapp.models import Order
from restapp.serializers import OrderSerializer
from restapp.models import Payment
from restapp.serializers import PaymentSerializer
from restapp.models import Feedback
from restapp.serializers import FeedbackSerializer

from restapp.models import FoodItem
from restapp.serializers import FoodItemSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer     
 
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class =RestaurantSerializer
    
   
   
class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    
        
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer   
        
class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer   
    
class FoodItemList(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    
class FoodItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    
from django.contrib.auth.models import User
from restapp.serializers import UserSerializer


    
from rest_framework import viewsets
 
class UserViewSet(viewsets.ReadOnlyModelViewSet):
     """
     This viewset automatically provides `list` and `retrieve` actions.
     """
     queryset = User.objects.all()
     serializer_class = UserSerializer    
    
class DemoFeedbackList(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    def get_queryset(self):
        """
        This view should return a list of all the feedbacks for
        the user as determined by the username portion of the URL.
        """
        userid = self.kwargs['userid']
        return Feedback.objects.filter(owner=userid)  
        
class FiltersList(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    def get_queryset(self):
        """
        This view should return a list of all the feedbacks for
        the user as determined by the username portion of the URL.
        """
        queryset = Feedback.objects.all()
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = queryset.filter(owner=userid)
            
        rating = self.request.query_params.get('rating', None)
        if rating is not None:
            queryset = queryset.filter(rating=rating)          
        return queryset        