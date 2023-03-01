from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('see_book/<int:id>', views.see_book, name='see_book'),
    path('register_book/', views.register_book, name='register_book'),
]
