from django.db import models

   
class Customer(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    phone = models.IntegerField( blank=True)
    email = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    address = models.CharField(max_length=200,blank=True, default='')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    pincode = models.IntegerField(blank=True)
    
class Restaurant(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    phone = models.IntegerField(blank=True)
    email = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    address = models.CharField(max_length=200,blank=True, default='')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    pincode = models.IntegerField(blank=True)    
    rating = models.IntegerField(blank=True)    

class Payment(models.Model):
    payMode = models.CharField(max_length=20,blank=False, default='') 
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)
    charges = models.IntegerField(default=False)
    payStatus = models.CharField(max_length=20,blank=False, default='') 
    test = models.IntegerField(default=False)
    owner = models.ForeignKey('auth.User', related_name='payments', on_delete=models.CASCADE)
    
class Order(models.Model):    
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)
    fooditem = models.ForeignKey('FoodItem', on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True)
    order_status = models.CharField(max_length=20,blank=False, default='') 
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)


class Feedback(models.Model):    
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=100,blank=False, default='') 
    rating = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='feedbacks', on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=20,blank=False, default='') 
   
class FoodItem(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    price = models.IntegerField(default=False)
    image = models.CharField(max_length=20,blank=False, default='')
    foodtype = models.CharField(max_length=20,blank=False, default='veg')
    is_available = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='fooditems', on_delete=models.CASCADE)
