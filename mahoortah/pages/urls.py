from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("products/",views.products,name='products'),
    path("articles/",views.articles,name="articles"),
    path('article/<int:id>/',views.getarticle,name="getarticle"),
    path("search/",views.searching,name="searching"),
    path('aboutUs/',views.aboutUs,name="aboutUs"),
    path('contact/',views.contact,name="contact"),
    path("product/<int:product_id>/",views.seeproduct,name="seeproduct"),
    path("products/<int:type_id>/",views.typefilter,name="typefilter"),
    path("pdf/",views.pdf_view,name="pdfreader"),
    path("articles/<int:article_id>/",views.seearticle,name="seearticle"),
    path("allprojects/",views.allprojects,name="allprojects"),
]
