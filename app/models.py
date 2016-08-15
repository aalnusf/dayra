from django.db import 
from django.utils import timezone  
from django.utils.http import urlquote  
from django.core.mail import send_mail  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class Category(models.model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.type

class Item(models.model):
    item = models.CharField(max_length= 255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey('app.Category')
    hours = models.FloatField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    cost_per_hour = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.item

 

