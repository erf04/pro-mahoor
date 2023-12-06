from django.shortcuts import render,redirect
from .models import article,product,ProImage,Type,Project
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
    theproducts1=product.objects.all()[0:3]
    theproducts2=product.objects.all()[3:6]
    types=Type.objects.all()
    projects=Project.objects.all()[0:3]
    articles1=article.objects.all()[:2]
    articles2=article.objects.all()[2:4]

    return render(request,"home2.html",{
        "pros":theproducts1,
        "pros2":theproducts2,
        "projects":projects,
        "articles1":articles1,
        "articles2":articles2
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

def seearticle(request,article_id):
    art=article.objects.get(pk=article_id)
    return render(request,'seearticle.html',{
        "art":art,
        
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
    similars=product.objects.filter(type__name=thepro.type.name)
    return render(request,'seeproduct.html',{
        "thepro":thepro,
        "images":images,
        "similars":similars,
    })

def typefilter(request,type_id):
    thepro=product.objects.filter(pk=type_id)
    return render(request,'products.html',{
        "products":thepro,
    })


def getarticle(request:HttpRequest,id):
    thearticle=article.objects.get(pk=id)
    return render(request,"getarticle.html",{
        "article":thearticle,
    })


def allprojects(request):
    projects=Project.objects.all()
    return render(request,"allprojects.html",{
        "projects":projects
    }) 
