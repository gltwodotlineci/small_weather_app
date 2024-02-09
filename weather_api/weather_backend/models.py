from django.db import models
from members.models import Customuser
import os, uuid
from solo.models import SingletonModel
from django.conf import settings

# We'll use configuration for the time zone and for
#the api_key
class Configuration(SingletonModel):
    time_zone = models.CharField(
        default="Europe/Paris",
        max_length=50
    )
    weather_api_key = models.CharField(max_length=150, blank=True, null=True)


# Create the categories model
class CateogryBlog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=30, default="General", verbose_name="The category")
    description = models.CharField(max_length=60, blank=False, null=False, verbose_name="Description")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='category', verbose_name="The category")

# Create the model of the blog post
class BlogPost(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="The Title")
    body = models.TextField(max_length=300, blank=False, null=False, verbose_name="The Blog Post Content")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False, related_name='blog', verbose_name="The author of the blog post")
    category = models.ForeignKey(CateogryBlog, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name="The category")


# ______________________ S T R I P E ______________________
# Creating the product model
class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=35, blank=False, null=False, verbose_name="name")
    description = models.CharField(max_length=75, blank=True, null=True, verbose_name="Description")
    activ = models.BooleanField(default=True, verbose_name="Activated")

    def __str__(self):
        return self.name


class Price(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Amount")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='prices', verbose_name="product")
    currency = models.CharField(max_length=3, default='EUR', verbose_name="Currency")
    nickname = models.CharField(max_length=55, blank=True, null=True, verbose_name="Short description of price")

    def __str__(self):
        return self.amount
