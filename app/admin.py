from django.contrib import admin
from app.models import Category, Item, Cart, CustomUser


# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CustomUser)

