from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Category, Item, Cart


# Create your views here.

# cart views/urls/template are not ready yet.

def add_to_cart(request, pk):

    context = {}

    cart_list = Cart.objects.get(user=request.user)

    items = Item.objects.get(pk=pk)

    cart_list.item.add(item)

    cart_list.save()

    return HttpResponseRedirect("/cart/")

def remove_from_cart(request, pk):

    context = {}

    cart_list = Cart.objects.get(user=request.user)

    items = Item.objects.get(pk=pk)

    cart_list.delete(item)

    return HttpResponseRedirect("/cart/")

def get_cart(request):

    context = {}

    context ['cart'] = Cart.objects.get(user=request.user)

    return render (request, 'cart.html', context)



def category_list(request):

    context = {}

    categories = Category.objects.all()

    context['categories'] = categories

    return render (request, 'category_list.html', context)

def item_list(request, pk):

    context = {}

    category = Category.objects.get(pk=pk)

    context['category'] = category

    context['category'] = Category.objects.get(pk=pk)


    return render (request, 'item_list.html', context)

def item_detail(request, pk):

    context = {}

    context['items'] = Item.objects.get(pk=pk)

    #context['category'] = Category.objects.get(pk=pk)

    return render (request, 'item_detail.html', context)
