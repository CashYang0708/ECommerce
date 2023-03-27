import datetime


# Create your models here.
from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.username

    #to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_member_by_username(username):
        try:
            return Member.objects.get(username= username)
        except:
            return False

    def isExists(self):
        if Member.objects.filter(username = self.username):
            return True

        return False

class Category(models.Model):
    name= models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='upload/products')

    @staticmethod
    def get_Product_by_id(ids):
        return Product.objects.filter (id__in=ids)
    @staticmethod
    def get_all_Product():
        return Product.objects.all()

    @staticmethod
    def get_all_Product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_Product()

class Decoration(models.Model):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='upload/decoration',null=True)

    def set_decoration(self):
        self.save()
    @staticmethod
    def get_decoration_by_member(username):
        return Decoration.objects.filter(member=username)

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_member(username):
        return Order.objects.filter(member=username).order_by('-date')