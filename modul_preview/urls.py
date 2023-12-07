from django.urls import path
from modul_preview.views import show_bacaan, show_bacaan_kreasi

app_name = 'modul_preview'

urlpatterns = [
    path('baca/<int:id>', show_bacaan, name='show_bacaan'),
    path('baca-kreasi/<int:id>', show_bacaan_kreasi, name='show_bacaan_kreasi'),
]