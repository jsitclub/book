from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=50)
    translator=models.CharField(max_length=50,null=True,default='')
    isbn=models.CharField(max_length=13,null=True,default='')
    page=models.IntegerField(null=True,default=0)
    publisher=models.CharField(max_length=50, null=True,default='')
    publishdate=models.DateField(null=True)
    created=models.DateTimeField(null=True)
    modified=models.DateTimeField(null=True)
    

class Category(models.Model):
    code=models.CharField(max_length=15,unique=True,null=False)
    content=models.CharField(max_length=50)  


class Book_Cate(models.Model):
    bookcode=models.IntegerField(null=False)
    catecode=models.CharField(max_length=15)
    