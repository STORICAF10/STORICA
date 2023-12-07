from django.shortcuts import render
from main.models import Buku, BukuKreasi
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from modul_baca.forms import KomentarForm, KomentarKreasiForm
from django.http import HttpResponseRedirect


@login_required(login_url='/login')
def show_create_komentar(request, buku_id):
    buku = Buku.objects.get(pk=buku_id)
    komentar = buku.komentar.all()

    if request.method == "POST":
        form = KomentarForm(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.user = request.user
            komentar.dari_buku = buku
            komentar.save()
            return HttpResponseRedirect(reverse('modul_baca:show_create_komentar', args=[buku_id]))
    else:
        form = KomentarForm()

    return render(request, 'komentar.html', {'buku': buku, 'komentars': komentar, 'form': form})


@login_required(login_url='/login')
def show_create_komentar_kreasi(request, buku_id):
    buku = BukuKreasi.objects.get(pk=buku_id)
    komentar = buku.komentar.all()

    if request.method == "POST":
        form = KomentarKreasiForm(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.user = request.user
            komentar.dari_buku = buku
            komentar.save()
            return HttpResponseRedirect(reverse('modul_baca:show_create_komentar_kreasi', args=[buku_id]))
    else:
        form = KomentarKreasiForm()

    return render(request, 'komentar_kreasi.html', {'karya': buku, 'komentars': komentar, 'form': form})