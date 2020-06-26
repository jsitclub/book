from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('setCategory/',views.setCategory),
    path('setBookInfo/',views.setBookInfo),
]