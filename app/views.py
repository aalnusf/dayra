from django.shortcuts import render, redirect, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Category, Item, Cart, CustomeUserManager, CustomUser
from django.db import IntegrityError
from forms import CustomUserCreationForm, CustomUserLoginForm, ContactForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
# Create your views here.

# cart views/urls/template are not ready yet.

# def get_cart(request):

#     context = {}

#     user = CustomUser.objects.get(pk=request.user.id)

#     context['cart'], created = Cart.objects.get_or_create(user=user)


#     print context['cart']

#     return render (request, 'cart.html', context)


def get_cart(request, pk):

    context = {}

    item = Item.objects.get(pk=pk)

    user = CustomUser.objects.get(pk=request.user.id)

    cart = Cart.objects.get(user=user)

    if cart == None:
        cart, created = Cart.objects.get_or_create(user=user)

    if request.method == "GET":
        cart.item.add(item)
    else:
        cart.item.remove(item)

    # total = 0

    # for item in cart.item.all():
    #     total += (item.cost_per_hour * item.hours)


    #     print total

    context['total'] = cart.total()

    context['cart'] = cart

    # context['item'] = item
    # return HttpResponseRedirect("/cart/")

    return render (request, 'cart.html', context)

# def remove_from_cart(request, pk):

#     context = {}

#     cart_list = Cart.objects.get(user=request.user)

#     items = Item.objects.get(pk=pk)

#     cart_list.remove(item)

#     return HttpResponseRedirect("/cart/")




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

    context['item'] = Item.objects.get(pk=pk)

    #context['category'] = Category.objects.get(pk=pk)

    return render (request, 'item_detail.html', context)



def signup(request):

  context = {}

  form = CustomUserCreationForm()

  context['form'] = form 

  if request.method == 'POST':
    
    form = CustomUserCreationForm(request.POST)

    if form.is_valid():

      print form.cleaned_data 
      # name = form.cleaned_data['name']
      email = form.cleaned_data.get('email', None)
      password = form.cleaned_data.get('password', None)


      try:
        form.save()
        # new_user = User.objects.create_user(email, password)
        context['valid'] = "Thank You For Signing Up and Welcome to Dayra!"
        
        # auth_user = authenticate(username=email, password=password)
        # login(request, auth_user)

        return HttpResponseRedirect('/category_list/')

      except IntegrityError as e:
        context['valid'] = "We know its annoying but, a User With That Name Already Exists"
        message = """
        We know its annoying but, a User With That Name Already Exists
        <a href= '/login_view/'>login<a>
        """

        return HttpResponse(message)
    else:
      context['valid'] = form.errors

  elif request.method == 'GET':
    context['valid'] = "Please join Dayra and Sign Up!"

  return render (request, 'signup.html', context)


def login_view(request):

    context = {}
    context['form'] = CustomUserLoginForm()

    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)
            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                print e
                message = """
                username or password incorrect, try again 
                <a href= '/login_view/'></a>
                """ 
                return HttpResponse(message) 
            return redirect ('/category_list/')
            
    return render(request, 'login_view.html', context)

  # context = {}

  # context['form'] = CustomUserLoginForm()

  # email = request.POST.get('email', None)
  # password = request.POST.get('password', None)

  # auth_user = authenticate(username=email, password=password)


  # # if auth_user is not None:
  # # if auth_user.is_active:
  #    # login(request, auth_user)
  #   if
  #    context['valid'] = "Login Successful"

  # return HttpResponseRedirect('/category_list/')

  #   # else:
  #   #   context['valid'] = "Invalid User"
  #     # message = 
  # else:
  #   context['valid'] = "Please enter a User Name"

  # return render (request, 'login_view.html', context)



def logout_view(request):

  logout(request)

  return HttpResponseRedirect('/login_view/')  


def about_view(request):

  context = {}
  
  return render (request, 'about.html', context)   

def how_view(request):

  context = {}
  
  return render (request, 'how.html', context)  

def contact(request):
   context = {}
   form_class = ContactForm()
   context['form'] = form_class
   
   return render(request, 'contact.html', context)   

    
