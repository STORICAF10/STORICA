from django.urls import path
from modul_baca.views import create_komentar_flutter, json_komentar, json_komentar_kreasi, show_create_komentar, show_create_komentar_kreasi

app_name = 'modul_baca'

urlpatterns = [
    path('komentar/<int:buku_id>/', show_create_komentar, name='show_create_komentar'),
    path('komentar-karya/<int:buku_id>/', show_create_komentar_kreasi, name='show_create_komentar_kreasi'),
    path('json-komentar/<int:buku_id>/', json_komentar, name='json_komentar'),
    path('json-komentar-kreasi/<int:buku_id>/', json_komentar_kreasi, name='json_komentar_kreasi'),
    path('create-komentar-flutter/', create_komentar_flutter, name='create_komentar_flutter'),
]