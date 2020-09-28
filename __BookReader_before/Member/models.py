from django.db import models

# Create your models here.

class Member(models.Model):
    
    id=models.CharField(max_length=20,primary_key=True)
    pw=models.CharField(max_length=70)
    email=models.CharField(max_length=50,unique=True,null=True,default='')
    nickname=models.CharField(max_length=30)
    
    status=models.CharField(max_length=10)  #정상,탈퇴,보류 등...
    created=models.DateTimeField(null=True)
    
class Member_Book(models.Model):
    Member_id=models.ForeignKey(Member,on_delete=models.SET_DEFAULT,default="remove_member")
    Book_code=models.IntegerField(null=False,default=0)
    
    state=models.CharField(max_length=20)   #10:관심 , 50: 읽는중 ,90:읽었음
    rating=models.IntegerField(null=True,default=0) #평점
    created=models.DateTimeField(null=True)