from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Buku, BukuKreasi
from main.forms import BukuForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/login')
def show_bacaan(request, id):
    buku = Buku.objects.get(pk = id)
    context = {
        'buku': buku,
    }
    return render(request, "bacaan.html", context)


@login_required(login_url='/login')
def show_bacaan_kreasi(request, id):
    karya = BukuKreasi.objects.get(pk = id)
    context = {
        'karya': karya,
    }
    return render(request, "bacaan_kreasi.html", context)