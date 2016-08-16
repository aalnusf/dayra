from django.shortcuts import render
from app.models import Category, Item


# Create your views here.

def category_list(request):

    context = {}

    categories = Category.objects.all()

    context['categories'] = categories

    return render (request, 'category_list.html', context)

def item_list(request):

    context = {}

    context['items'] = Item.objects.all()

    return render (request, 'item_list.html', context)

def item_detail(request, pk):

    context = {}

    context['items'] = Item.objects.get(pk=pk)

    return render (request, 'item_detail.html', context)
