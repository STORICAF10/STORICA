from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    judul = models.CharField(max_length=255, null=True, blank=True)
    jumlah_halaman = models.PositiveIntegerField(null=True, blank=True)
    bahasa = models.CharField(max_length=50, null=True, blank=True)
    penulis = models.CharField(max_length=255, null=True, blank=True)
    penerbit = models.CharField(max_length=255, null=True, blank=True)
    jumlah_review = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    gambar = models.URLField(null=True, blank=True)
    tanggal_terbit = models.DateField(null=True, blank=True)
    buku_favorites = models.ManyToManyField(User)
    isi_buku = models.TextField(default="Sayangnya buku ini belum tersedia :(, silahkan coba buku lainnya")


class BukuKreasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    judul = models.CharField(max_length=255, null=True, blank=True)
    jumlah_halaman = models.PositiveIntegerField(null=True, blank=True)
    bahasa = models.CharField(max_length=50, null=True, blank=True)
    penulis = models.CharField(max_length=255, null=True, blank=True)
    penerbit = models.CharField(max_length=255, null=True, blank=True)
    jumlah_review = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    gambar = models.URLField(null=True, blank=True)
    tanggal_terbit = models.DateField(null=True, blank=True)
    is_published = models.BooleanField()
    isi_buku = models.TextField(null="",blank="")


    # Representasi teks model 
    def __str__(self):
        return self.judul

class level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    buku_total = models.PositiveIntegerField()
    batas_atas = models.PositiveIntegerField()
    persen = models.PositiveIntegerField()


class quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kata_kata = models.TextField()

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gambar = models.URLField(null=True, blank=True)