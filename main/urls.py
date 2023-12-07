from django.urls import path
from main.views import *
from main.views import add_quotes_ajax
from . import views

app_name = 'main'

urlpatterns = [
    path('create-quotes-ajax/',add_quotes_ajax,name="add_quotes_ajax"),
    path('filter-inggris/',filter_bahasa_inggris,name='filter_inggris'),
    path('filter-karya/',filter_buku_karya,name='filter_karya'),
    path('filter-empat/',filter_bintang_empat,name='filter_empat'),
    path('my-quotes/',show_my_quotes,name='show_my_quotes'),
    path('koleksi-buku/',show_semua, name ='show_semua'),
    path('login', login_user, name='login'),
    path('', show_main, name='show_main'),
    path('create-buku', create_buku, name='create_buku'),
    path('xml/', show_xml, name='show_xml'), 
    path('buku-json/', show_buku_json, name='show_buku_json'),
    path('bukukreasi-json/', show_buku_kreasi_json, name='show_bukukreasi_json'),
    path('myquotes-json/', show_my_quotes_json, name='show_myquotes_json'),
    path('profile-json/', show_profile_json, name='show_profile_json'), 
    path('quotes-json/', show_quotes_json, name='show_quotes_json'),
    path('level-json/', show_level_json, name='show_level_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('edit-buku/<int:id>', edit_buku, name='edit_buku'),
    path('delete/<int:id>', delete_buku, name='delete_buku'),
    path('preview/<int:id>', show_preview, name='show_preview'),
    path('preview-kreasi/<int:id>', show_preview_kreasi, name='show_preview_kreasi'),
    path('get-quotes-jason',get_quotes_json,name="get_quotes_json"),
    path('delete-quotes/<int:id>', delete_quotes, name='delete_quotes'),
    path("create-isi-buku", views.createIsiBuku, name="create_isi_buku"),
    path("create-isi-buku-baru", views.createIsiBuku, name="create_isi_buku_baru"),
    path("publish/<int:id_buku>", views.publish, name="publish"),
    path("create-isi-buku-saved/<int:id_buku>", views.autoSave, name="autoSave"),
    path("create-buku-baru", views.create_buku_baru, name='create_buku_baru'),
]