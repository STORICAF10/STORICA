from django.urls import path
from modul_baca.views import show_create_komentar, show_create_komentar_kreasi
from modul_preview.views import show_bacaan

app_name = 'modul_baca'

urlpatterns = [
    path('komentar/<int:buku_id>/', show_create_komentar, name='show_create_komentar'),
    path('komentar-karya/<int:buku_id>/', show_create_komentar_kreasi, name='show_create_komentar_kreasi'),
]