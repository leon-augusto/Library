from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('valid_register/', views.valid_register, name='valid_register'),
    path('valid_login/', views.valid_login, name='valid_login'),
    path('logout/', views.logout, name='logout'),
]
