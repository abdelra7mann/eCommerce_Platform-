from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Customer(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=155,null=True)
    email = models.CharField(max_length=155,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    storage_Capacity = models.CharField(max_length=200,blank=True,null=True)
    size = models.CharField(max_length=200,blank=True,null=True)
    battery  = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.name
    @property
    def imageUrl(self):
        try : 
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complate = models.BooleanField(default=False)
    transaction_id =models.CharField(max_length=155,null=True)
    
    def __str__(self):
        return str(self.id)


    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
        

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all() #هترجع اي حاجه ليها علاقه ب الاوردر زي الاوردر ايتم والادرس
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    date_aded = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    def __str__(self) -> str:
        return self.product.name

class ShippingAddress(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    date_aded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address

 
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username, email=instance.email)