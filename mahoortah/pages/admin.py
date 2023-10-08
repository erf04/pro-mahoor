from django.contrib import admin
from .models import article,product,ProImage,Type

# Register your models here.
admin.site.register(article)
admin.site.register(product)
admin.site.register(ProImage)
admin.site.register(Type)