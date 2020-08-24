from django.db import models

# Create your models here.

class Book(models.Model):
    code=models.AutoField(primary_key=True,default='')
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=50)
    translator=models.CharField(max_length=50,null=True,default='')
    isbn=models.CharField(max_length=13,null=True,default='')
    page=models.IntegerField(null=True,default=0)
    publisher=models.CharField(max_length=50, null=True,default='')
    publishdate=models.DateField(null=True)
    created=models.DateTimeField(null=True)

class BookCover(models.Model):
    code=models.OneToOneField('Book', on_delete=models.CASCADE,default="")
    cover=models.ImageField(upload_to='book_covers/')
    created=models.DateTimeField(null=True)

class Category(models.Model):
    code=models.CharField(primary_key=True,default='',max_length=21)
    content=models.CharField(max_length=50) 
    
class Book_Cate(models.Model):
    bookcode=models.ForeignKey('Book', on_delete=models.CASCADE,default="")
    catecode=models.CharField(max_length=21)
    