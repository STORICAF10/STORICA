from django.forms import ModelForm
from main.models import Buku
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class BukuForm(ModelForm):
    class Meta:
        model = Buku
        fields = [
            "id_buku",
            "judul",
            "jumlah_halaman",
            "bahasa",
            "penulis",
            "penerbit",
            "jumlah_review",
            "rating",
            "gambar",
            "tanggal_terbit",
            "isi_buku",
        ]
