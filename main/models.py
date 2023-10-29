from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms

dateNow = datetime.now()


class Buku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_buku = models.PositiveIntegerField(null=True, blank=True)
    judul = models.CharField(max_length=255, null=True, blank=True)
    jumlah_halaman = models.PositiveIntegerField(null=True, blank=True)
    bahasa = models.CharField(max_length=50, null=True, blank=True)
    penulis = models.CharField(max_length=255, null=True, blank=True)
    penerbit = models.CharField(max_length=255, null=True, blank=True)
    jumlah_review = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    gambar = models.ImageField(null=True, blank=True)
    tanggal_terbit = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    isi_buku = models.TextField(null=True, blank=True)

    # Representasi teks model
    # def __str__(self):
    #     self.fields["tanggal_terbit"].widget = forms.DateInput(attrs={"type": "date"})
    #     return self.judul
