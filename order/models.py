from django.db import models

from users.models import (
    Customer,
    Vendor,
)

#Create your models here.
class Order(models.Model):
    order_date = models.DateTimeField(
        auto_now_add=True,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        related_name='order',
    )
    total = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False,
    )
    payment_method = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.id

class OrderItem(models.Model):
    item = models.CharField(
        max_length=255,
        blank=False,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False,
    )
    vendor = models.ForeignKey(
        Vendor,
        null=True,
        related_name='vendor',
        on_delete=models.SET_NULL,
    )
    order = models.ForeignKey(
        Order,
        related_name='item',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.item
