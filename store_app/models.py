from django.db import models
from django.utils import timezone
import uuid
import time

def generate_unique_hash():    
    random_hash = str(uuid.uuid4().int)[:6]    
    timestamp = str(int(time.time()))    
    unique_hash = f"{random_hash}_{timestamp}"
    return unique_hash

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    

    
class Brand(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class Filter_Price(models.Model):
    Filter_PRICE = (
        ('0 TO 1000','0 TO 1000'),
        ('1000 TO 10000','1000 TO 10000'),
        ('10000 TO 20000','10000 TO 20000'),
        ('20000 TO 30000','20000 TO 30000'),
        ('30000 TO 40000','30000 TO 40000'),
        ('40000 TO 50000','40000 TO 50000'),
        ('50000 TO 100000+','50000 TO 100000+'),
    )
    price = models.CharField(choices = Filter_PRICE,max_length = 60)

    def __str__(self):
        return self.price

class Product(models.Model):
    CONDITION = (("NEW","NEW"),("OLD","OLD"))
    STOCK = (("IN STOCK","IN STOCK"),("OUT OF STOCK","OUT OF STOCK"))
    STATUS = (("PUBLISH","PUBLISH"),("DRAFT","DRAFT"))

    unique_id = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='Product_images/img')
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    condition = models.CharField(choices = CONDITION,max_length = 100)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices = STOCK,max_length  = 200)
    status = models.CharField(choices = STATUS,max_length = 200)
    created_date = models.DateTimeField(default = timezone.now)

    categories = models.ForeignKey(Categories,on_delete = models.CASCADE) 
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    color = models.ForeignKey(Color,on_delete = models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete = models.CASCADE)


        
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = generate_unique_hash()
        super(Product, self).save(*args, **kwargs)
        

    def __str__(self):
        return self.name
    
class Images(models.Model):
    image = models.ImageField(upload_to="Product_images/img")
    product = models.ForeignKey(Product,on_delete = models.CASCADE)



class Tag(models.Model):
    name = models.CharField(max_length = 200)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)

