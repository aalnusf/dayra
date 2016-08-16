from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Category, Item
from app.forms import 


# Create your views here.

def signup(request):

    context = {}

    form = UserSignUp()

    context['form'] = form 

    if request.method == 'POST':

        form = UserSignUp(request.POST)

        if form.is_valid():
            
            print form.cleaned_data 
            name = form.cleaned_data['name']
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)


            try:
                new_user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank You For Signing Up and Welcome to Dayra!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/category_list/')

              except IntegrityError, e:
                context['valid'] = "We know its annoying but, a User With That Name Already Exists"

            else:
              context['valid'] = form.errors

            if request.method == 'GET':
               context['valid'] = "Please join Dayra and Sign Up!"

               return render_to_response('signup.html', context, context_instance=RequestContext(request))


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


  return render_to_response('login_view.html', context, context_instance=RequestContext(request))



def logout_view(request):

  logout(request)

  return HttpResponseRedirect('/login_view/')  

