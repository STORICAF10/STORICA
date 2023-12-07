from django.forms import ModelForm
from modul_baca.models import Komentar, KomentarKreasi

class KomentarForm(ModelForm):
    class Meta:
        model = Komentar
        fields = ["isi_komentar", "rating"]

class KomentarKreasiForm(ModelForm):
    class Meta:
        model = KomentarKreasi
        fields = ["isi_komentar", "rating"]