from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
 
]
