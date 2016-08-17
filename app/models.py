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


class CustomUserManager(BaseUserManager):  

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields): # any def with _ after it is a private class, you can not call it in any applications only inside the class it self
        now =  timezone.now()
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)  # to make email login not case sensitive
        user = self.model(email=email,
                            is_staff=is_staff,
                            is_active=True,
                            is_superuser=is_superuser,
                            last_login=now,
                            **extra_fields
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields): 
        return self._create_user(email, password, True, True, **extra_fields)  

class CustomUser(AbstractBaseUser, PermissionsMixin):     # point is to login with email rather than username.
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='first name',max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='last name',max_length=255, blank=True, null=True)
    company = models.CharField(verbose_name='company',max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(verbose_name='staff status', default=False)
    is_active = models.BooleanField(verbose_name='active', default=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name= 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):    
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):  
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])





















 

