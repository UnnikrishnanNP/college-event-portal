from django.urls import path
from . import views

urlpatterns = [
    path('', views.events),
    path('products/', views.products),
    path('customers/', views.customers),

]
