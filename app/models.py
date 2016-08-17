from django.db import models
from django.utils import timezone  
from django.utils.http import urlquote  
from django.core.mail import send_mail  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class Category(models.Model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.type

class Item(models.Model):
    name = models.CharField(max_length= 255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey('app.Category', null=True, blank=True)
    hours = models.FloatField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    cost_per_hour = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name

class Cart(models.Model):
    item = models.ManyToManyField('app.Item', null=True, blank=True)
   #user = models.OneToOneField('app.CustomUser', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)




