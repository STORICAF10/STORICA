from django.urls import path
from modul_preview.views import show_bacaan

app_name = 'modul_preview'

urlpatterns = [
    path('baca/<int:id>', show_bacaan, name='show_bacaan'),
]