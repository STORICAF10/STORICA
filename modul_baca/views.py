from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from modul_baca.forms import KomentarForm, KomentarKreasiForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
import json
from django.http import JsonResponse
from main.models import Buku, BukuKreasi
from modul_baca.models import Komentar, KomentarKreasi
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
def show_create_komentar(request, buku_id):
    buku = Buku.objects.get(pk=buku_id)
    komentar = buku.komentar.all()

    if request.method == "POST":
        form = KomentarForm(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False)
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
            komentar.dari_buku = buku
            komentar.save()
            return HttpResponseRedirect(reverse('modul_baca:show_create_komentar_kreasi', args=[buku_id]))
    else:
        form = KomentarKreasiForm()

    return render(request, 'komentar_kreasi.html', {'karya': buku, 'komentars': komentar, 'form': form})


def json_komentar(request, buku_id):
    komentar_buku = Buku.objects.get(pk=buku_id).komentar.all().order_by('-tgl_komentar')
    return HttpResponse(serializers.serialize("json", komentar_buku))


def json_komentar_kreasi(request, buku_id):
    komentar_buku_kreasi = BukuKreasi.objects.get(pk=buku_id).komentar.all().order_by('-tgl_komentar')
    return HttpResponse(serializers.serialize("json", komentar_buku_kreasi))


@csrf_exempt
def create_komentar_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        buku = Buku.objects.get(pk=data["dari_buku"])

        new_komentar = Komentar.objects.create(
            isi_komentar = data["isi_komentar"],
            rating = int(data["rating"]),
            dari_buku = buku,
        )

        new_komentar.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def create_komentar_kreasi_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        buku = BukuKreasi.objects.get(pk=data["dari_buku"])

        new_komentar = KomentarKreasi.objects.create(
            isi_komentar = data["isi_komentar"],
            rating = int(data["rating"]),
            dari_buku = buku,
        )

        new_komentar.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)