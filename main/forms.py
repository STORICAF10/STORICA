from django.forms import ModelForm
from main.models import BukuKreasi

class BukuForm(ModelForm):
    class Meta:
        model = BukuKreasi
        fields = ["judul", "jumlah_halaman", "bahasa", "penulis", "penerbit", "jumlah_review", "rating", "gambar", "tanggal_terbit", "isi_buku", "is_published"]