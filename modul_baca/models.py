from django.db import models
from django.contrib.auth.models import User
from main.models import Buku

class Komentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    tgl_komentar = models.DateTimeField(auto_now_add=True)
    isi_komentar = models.TextField()
    dari_buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='komentar')