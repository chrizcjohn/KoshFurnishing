from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name



class Discount(models.Model):
    discount = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.discount

class Material(models.Model):
    material_name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.material_name

class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=20, null=True)
    phone = models.IntegerField(null=True)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
           return True
        return False
           
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL , null=True ,blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL , null=True ,blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL , null=True ,blank=True)
    image = models.ImageField(null=True,blank =True)
    
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids )


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id: 
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=200,default='',blank =True)
    phone = models.IntegerField(default=0, blank =True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')


    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True , blank = True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

