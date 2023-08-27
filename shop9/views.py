from django.shortcuts import render,HttpResponse, redirect
from .models import Product,Category
from django.contrib.auth.models import User,auth
from django.contrib import auth



# Create your views here.
def cats(request):
    return render(request,'base.html')

def index(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'products':products,'category':category})

def category(request,category):
    category=Category.objects.get(category)
    products = Product.objects.filter(category)
    return render(request,'index.html',{'products':products})

def register(request):
    if request.method =="POST":          
        first_name = request.POST.get('first_name')
        second_name=request.POST.get('second_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')        
        if password1==password2:
            if User.objects.filter(email=email).exists():
                return render(request,'base.html')
            else:
                user=User.objects.create_user(username, password1, email)
                user.save()
                return render(request,'register.html')
        else:
            return render(request,'base.html')
            # print('password not matching')
            # return HttpResponseRedirect('/') 
    else:
        return render(request,'register.html')

        
         

        # return redirect('/')
    endif
    
    

   

   

