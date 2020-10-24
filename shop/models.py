from django.db import models

# Create your models here.

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    product_dec=models.CharField(max_length=300)
    publish_date=models.DateField()
    category=models.CharField(max_length=50, default="")
    subCategory=models.CharField(max_length=50, default="")
    images=models.ImageField( upload_to='shop/images', height_field=None, width_field=None, max_length=None,default="")
    price=models.IntegerField(default="0")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    itemsJson=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timeStamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    