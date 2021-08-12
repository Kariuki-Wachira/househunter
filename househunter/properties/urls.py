from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.homepage, name='homepage'),
    path('property/<str:pk>/', views.viewProperty, name='property'),
    path('add/', views.addProperty, name='add'),
]