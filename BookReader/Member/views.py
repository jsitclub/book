from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import *
import hashlib
    
##===============================

# Create your views here.
def signup(request):
    return render(request,"Member/signup.html")

def signup_(request):
    id=request.POST['Username']
    pw=request.POST['password']
    email=request.POST['email']
    
    
    if Member.objects.filter(id=id).exists():    
        return HttpResponse("data exitst :id="+id)
    elif Member.objects.filter(email=email).exists():    
        return HttpResponse("data exitst :email="+email)
        
    else:
        #pw 암호화
        encoded_pw=pw.encode()
        encrypted_pw=hashlib.sha256(encoded_pw).hexdigest()
        
        new_member=Member(id=id, pw=encrypted_pw, email=email)
        new_member.save()
        return HttpResponse("insert new data:id="+id)
    

def signin(request):
    return render(request,"Member/signin.html")

def signin_(request):
    id=request.POST['Username']
    pw=request.POST['password']
    
    #pw 암호화
    encoded_pw=pw.encode()
    encrypted_pw=hashlib.sha256(encoded_pw).hexdigest()
    
    if Member.objects.filter(id=id,pw=encrypted_pw).exists():  
        print("login OK")
        #return render(request,"Book/bookshelf.html")
        return HttpResponseRedirect(reverse('bookshelf'))
    
    else:    
        return HttpResponse("data not exitst")
 
def bookshelf(request):
    return render(request,"Member/bookshelf.html")
   