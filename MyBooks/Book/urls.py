from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),   
    path('setCategory/',views.setCategory),
    path('setBookInfo/',views.setBookInfo),
    path('findBook_kakao/',views.findBook_kakao),
    path('findBook_naver/',views.findBook_naver),
]