from django.forms import ModelForm
from main.models import Buku

class BukuForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["judul", "jumlah_halaman", "bahasa", "penulis", "penerbit", "jumlah_review", "rating", "gambar", "tanggal_terbit", "isi_buku"]