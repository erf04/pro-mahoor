from django.shortcuts import render,redirect
from .models import article,product,ProImage
from django.contrib import messages
from django.http import HttpRequest
from django.core.paginator import Paginator
from django.http import FileResponse, Http404

def pdf_view(request):
    try:
        return FileResponse(open('c.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    

def home(request):
    theproducts=product.objects.all()
    return render(request,"home2.html",{
        "pros":theproducts,
    })

def products(request):
    theproducts=product.objects.all()
    return render(request,'products.html',{
        "products":theproducts,
    })

def articles(request):
    allarticles=article.objects.all()
    # print(allarticles.count)
    colors=("blue","red","green","yellow")
    list=zip(allarticles,colors)
    return render(request,'articles.html',{
        "list":list,

    })


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
    images=ProImage.objects.filter(pro_id=product_id)
    return render(request,'seeproduct.html',{
        "thepro":thepro,
        "images":images,
        
    })

def typefilter(request,product_type):
    thepro=product.objects.filter(type=product_type)
    return render(request,'products.html',{
        "theproducts":thepro,
    })


def getarticle(request:HttpRequest,id):
    thearticle=article.objects.get(pk=id)
    return render(request,"getarticle.html",{
        "article":thearticle,
    })
