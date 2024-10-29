from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login, name='login'),  # Login page
    path('delete_user/<id>', views.delete_user, name='delete'),  # Delete user
    path('update/<int:id>/', views.update_user, name='update'),

]
