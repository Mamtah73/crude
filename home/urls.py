from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addnew/', views.addnew, name='addnew'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
]