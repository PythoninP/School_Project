from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('Hlogin', views.Hlogin, name='Hlogin'),
    path('new', views.new, name='new'),
    path('logout', views.logout, name='logout'),
    path('order', views.order, name='order'),
]