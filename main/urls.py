from django.urls import path
from main.views import show_main, create_buku, show_preview, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user
from main.views import logout_user
from main.views import edit_buku
from main.views import delete_buku

app_name = 'main'

urlpatterns = [
    path('login', login_user, name='login'),
    path('', show_main, name='show_main'),
    path('create-buku', create_buku, name='create_buku'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('edit-buku/<int:id>', edit_buku, name='edit_buku'),
    path('delete/<int:id>', delete_buku, name='delete_buku'),
    path('preview/<int:id>', show_preview, name='show_preview'),
]