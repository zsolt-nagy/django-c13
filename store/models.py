from django.db import models
import datetime

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description=models.TextField()
    publish_date = models.DateField(default=datetime.date.today)

class Coupon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    coupon_code = models.CharField(max_length=40)
    expiry_date = models.DateField(default=datetime.date.today)