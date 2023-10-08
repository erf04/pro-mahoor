from django.shortcuts import render,redirect
from .models import article,product,ProImage
from django.contrib import messages
from django.http import HttpRequest

def home(request):
    return render(request,"home2.html",{})

def products(request):
    theproducts=product.objects.all()
    return render(request,'products.html',{
        "theproducts":theproducts,
    })

def articles(request):
    return render(request,'articles.html',{})


def searching(request:HttpRequest):
    if request.method=="POST":
        key=request.POST["searchkey"]
        try :
            theproducts=product.objects.filter(title__contains=key) | product.objects.filter(type__name__contains=key) | product.objects.filter(text__contains=key)
            thearticles=article.objects.filter(title__contains=key) | article.objects.filter(text__contains=key)
        except:
            messages.success(request,"key is not valid")
            
    return render(request,'searching.html',{
        "theproducts":theproducts,
        "thearticles":thearticles,
        "key":key,
    })


def aboutUs(request):
    return render(request,"aboutus.html",{
        
    })

def projects(request):
    pass

def contact(request):
    pass 

def seeproduct(request,product_id):
    thepro=product.objects.get(pk=product_id)
    return render(request,'seeproduct.html',{
        "thepro":thepro,
    })

def typefilter(request,product_type):
    thepro=product.objects.filter(type=product_type)
    return render(request,'products.html',{
        "theproducts":thepro,
    })