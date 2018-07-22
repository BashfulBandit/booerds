from django.db import models

#Create your models here.
#customer ID
#book ID
#vendor ID

# Create your models here.

class Order(models.Model):
    customer_id = models.IntegerField(
        blank=False
    )

    order_total = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False
    )

class Order_Detail(models.Model):
     
    book_id = models.IntegerField(
        blank=False
    )
    vendor_id = models.IntegerField(
        blank=False
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    
