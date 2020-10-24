from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="shopeHome"),
    path('about', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUS"),
    path('tracker/', views.tracker,name="Tracker"),
    path('search/', views.search,name="Search"),
    path('product/<int:id>', views.productView,name="productView"),
    path('checkout/', views.checkout,name="Checkout"),
    path('handlerequest/', views.handlerequest,name="Handel Request"),
]
