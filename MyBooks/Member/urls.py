from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('signup/signup_/',views.signup_),
    path('signin/',views.signin,name="signin"),
    path('signin/signin_/',views.signin_),
    path('bookshelf/',views.bookshelf,name="bookshelf"),
    
]