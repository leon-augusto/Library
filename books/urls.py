from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('see_book/<int:id>', views.see_book, name='see_book'),
    path('register_book/', views.register_book, name='register_book'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_borrowing/', views.create_borrowing, name='create_borrowing'),
    path('remove_book/<int:id>', views.remove_book, name='remove_book'),
]
