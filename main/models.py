from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=255)
    jumlah_halaman = models.PositiveIntegerField()
    bahasa = models.CharField(max_length=50)
    penulis = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    jumlah_review = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    gambar = models.URLField()
    tanggal_terbit = models.DateField()
    isi_buku = models.TextField()

    # Representasi teks model 
    def __str__(self):
        return self.judul