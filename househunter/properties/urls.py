from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('wishlist/',views.viewmywishlist,name='wishlist'),
    path("addWishlist/<str:pk>/",views.addToWishlist, name="addWish" ),

    path('staffrequest/', views.staffrequest, name='staffrequest'),
    path('makerequest/', views.sentrequest, name='makerequest'),
    path('', views.homepage, name='homepage'),
    path('property/<str:pk>/', views.viewProperty, name='property'),
    path('add/', views.addProperty, name='add'),
]