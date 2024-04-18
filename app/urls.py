from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('detail/<int:pk>',views.detail_view,name='detail'),
    path('update/<int:pk>',views.update_view,name='update'),
    path('delete/<int:pk>',views.delete_view,name='delete'),
    path('add_record/',views.add_record,name='add-record'),
 
]
