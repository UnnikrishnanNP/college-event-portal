from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('new_event/', views.new_event, name='new_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event')

]
# tba is given so that in future to change its name
