from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_profile', views.userProfile, name='user_profile'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('events/', views.events, name='events'),
    path('new_event/', views.newEvent, name='new_event'),
    path('register_event/<str:pk>/', views.registerEvent, name='register_event'),
    path('unregister/<str:pk>/', views.unregisterEvent, name='unregister'),
    path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event')

]
# tba is given so that in future to change its name
