from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('property/<str:pk>/', views.viewProperty, name='property'),
    path('add/', views.addProperty, name='add'),
]