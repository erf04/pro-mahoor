from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Fahome"),
    path("products/",views.products,name='Faproducts'),
    path("articles/",views.articles,name="Faarticles"),
    path('article/<int:id>/',views.getarticle,name="Fagetarticle"),
    path("search/",views.searching,name="Fasearching"),
    path('aboutUs/',views.aboutUs,name="FaaboutUs"),
    path('contact/',views.contact,name="Facontact"),
    path("product/<int:product_id>/",views.seeproduct,name="Faseeproduct"),
    path("products/<int:type_id>/",views.typefilter,name="Fatypefilter"),
    path("pdf/",views.pdf_view,name="pdfreader"),
    path("articles/<int:article_id>/",views.seearticle,name="Faseearticle"),
    path("allprojects/",views.allprojects,name="Faallprojects"),
]
