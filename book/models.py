from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length = 13)
    author = models.TextField()
    title = models.TextField()
    image = models.ImageField(upload_to = "images/")
    subject = models.TextField()
    sale_price = models.FloatField()
    vendor_price = models.FloatField()
    summary = models.TextField()