from django.forms import ModelForm
from modul_baca.models import Komentar

class KomentarForm(ModelForm):
    class Meta:
        model = Komentar
        fields = ["isi_komentar", "rating"]