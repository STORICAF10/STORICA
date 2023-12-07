from django.urls import path
from modul_favorites.views import *

app_name = 'modul_favorites'

urlpatterns = [
    path('show_favorites/', show_favorites, name='show_favorites'),
    path('add_favorites/<int:id>', add_favorites, name='add_favorites'),
    path('remove_favorites/<int:id>', remove_favorites, name='remove_favorites'),
]