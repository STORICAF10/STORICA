from django.urls import path
from main.views import show_main, create_buku, show_preview, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user
from main.views import logout_user
from main.views import edit_buku
from main.views import delete_buku
from modul_favorites.views import *

app_name = 'modul_favorites'

urlpatterns = [
    path('show_favorites/', show_favorites, name='show_favorites'),
    path('add_to_favorites/<str:nama>/<int:id>', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<str:nama>/<int:id>', remove_from_favorites, name='remove_from_favorites'),
    path('add_favorites/<int:id>', add_favorites, name='add_favorites'),
    path('remove_favorites/<int:id>', remove_favorites, name='remove_favorites'),
    path('show_favorites_json/<str:nama>', show_favorites_json, name='show_favorites_json'),
    path('check_favorite/<str:nama>/<int:id>', check_favorite, name='check_favorite'),
]