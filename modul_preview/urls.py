from django.urls import path
from main.views import show_main, create_buku, show_preview, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user
from main.views import logout_user
from main.views import edit_buku
from main.views import delete_buku
from modul_preview.views import show_bacaan

app_name = 'modul_preview'

urlpatterns = [
    path('baca/<int:id>', show_bacaan, name='show_bacaan'),
]