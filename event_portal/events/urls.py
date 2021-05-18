from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('events/', views.events),
    path('tba/', views.tba),

]
# tba is given so that in future to change its name