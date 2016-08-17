from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Category,Item, CustomUser, CustomUserManager
from app.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm




# # Create your views here.

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



def sign_up(request):

    context = {}


    context['form'] = CustomUserCreationForm() 

    if request.method == 'POST':

        form =CustomUserCreationForm(request.POST)

        if form.is_valid():
            
            print form.cleaned_data 
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)


            try:
                new_user = User.objects.create_user(email, password)
                context['valid'] = "Thank You For Signing Up and Welcome to Dayra!"

                auth_user = authenticate(username=email, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/category_list/')

            except IntegrityError, e:
                context['valid'] = "We know its annoying but, a User With That Name Already Exists"

        else:
            context['valid'] = form.errors

        return render(request, 'signup.html', context)


    if request.method == 'GET':
       context['valid'] = "Please join Dayra and Sign Up!"

       return render(request, 'signup.html', context)


def login_view(request):

    context = {}

    context['form'] = UserLogin()

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    auth_user = authenticate(username=username, password=password)

    if auth_user is not None:
      if auth_user.is_active:
        login(request, auth_user)
        context['valid'] = "Login Successful"

        return HttpResponseRedirect('/category_list/')
      else:
        context['valid'] = "Invalid User"
    else:
      context['valid'] = "Please enter a User Name"


    return render(request, 'login_view.html', context)



def logout_view(request):

  logout(request)

  return HttpResponseRedirect('/login_view/')  

