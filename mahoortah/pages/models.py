from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Type(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class product(models.Model):
    title=models.CharField(max_length=100)
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    text=models.CharField(max_length=1000)
    main_image=models.ImageField(upload_to="uploadedimages/")
    def __str__(self):
        return self.title


class ProImage(models.Model):
    images=models.ImageField(upload_to="uploadedimages/")
    pro_id=models.ForeignKey(product,on_delete=models.CASCADE)


class article(models.Model):
    title=models.CharField(max_length=100)
    text=models.CharField(max_length=1000)
    date=models.DateField()
    #author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    Name=models.CharField(max_length=1000)
    Email=models.EmailField()
    Comment=models.CharField(max_length=20000)
    def __str__(self) -> str:
        return self.Name
    
class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    image=models.ImageField(upload_to="uploadedimages/")

    def __str__(self) -> str:
        return self.name