from django.urls import path
from restapp import views
from .views import UserViewSet, OrderViewSet
from rest_framework import renderers
from rest_framework import viewsets
#from django.conf.urls import url 

from restapp import views_authentication

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapp import views

from rest_framework.documentation import include_docs_urls

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

orders_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/core/orders', views.OrderViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/core/customers/', views.CustomerList.as_view()),
    path('api/core/customers/<int:pk>/', views.CustomerDetail.as_view()),
    
    path('api/core/cities/', views.CityList.as_view()),
    path('api/core/cities/<int:pk>/', views.CityDetail.as_view()),    
       
    path('api/core/restaurants/', views.RestaurantList.as_view())  ,

    path('api/core/orders/',orders_list, name='orders-list')  ,
    path('api/core/orders/<int:pk>', order_detail,name='order-details'),     
    
    path('api/core/payments/', views.PaymentList.as_view())  ,
    path('api/core/payments/<int:pk>', views.PaymentDetail.as_view()),
    
    path('api/core/feedbacks/', views.FeedbackList.as_view())  ,
    path('api/core/feedbacks/<int:pk>', views.FeedbackDetail.as_view()),  
    
    path('api/core/fooditems/', views.FoodItemList.as_view())  ,
    path('api/core/fooditems/<int:pk>', views.FoodItemDetail.as_view()),
    
    path('api/authentication/registration/', views_authentication.register)  ,
    path('api/authentication/login/', views_authentication.login)  ,
    path('api/authentication/change_password/', views_authentication.change_password)  ,

    path(r'feedbacks/(?P<userid>.+)/$', views.DemoFeedbackList.as_view()), 
    
    path(r'api/core/filters', views.FiltersList.as_view()),
    
    path('', include(router.urls)),
    
    path(r'docs/', include_docs_urls(title='Helpdesk API')),
]     