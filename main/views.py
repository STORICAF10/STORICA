from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import *
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
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound



def show_main(request):
    karya_pengguna = BukuKreasi.objects.all().order_by('jumlah_review')
    bukus = Buku.objects.all().order_by('judul')
    kata_bijak = quotes.objects.all()

    if ('last_login' in request.COOKIES):
        context = {
            'kata_bijak':kata_bijak,
            'pengguna' : request.user.username,
            'last_login' : request.COOKIES['last_login'],
            'bukus': bukus,
            'karya': karya_pengguna
        }
    else:
        context = {
            'kata_bijak':kata_bijak,
            'bukus': bukus,
            'karya': karya_pengguna
        }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_buku(request):
    if request.method == "POST":
        form = BukuForm(request.POST, request.FILES)
        if form.is_valid():
            buku = form.save(commit=False)
            buku.user = request.user
            buku.save()
            return HttpResponseRedirect(reverse('main:show_main'))

    else:
        form = BukuForm()

    context = {'form': form}
    return render(request, "create_buku.html", context)

@csrf_exempt
def add_quotes_ajax(request):
    if request.method == 'POST':
        kata = request.POST.get("kata")
        user = request.user

        new_quotes = quotes(kata_kata=kata, user=user)
        new_quotes.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_my_quotes(request):
    kata_saya = quotes.objects.filter(User=request.user)

    context = {
        'kata_saya':kata_saya
    }

    return render(request,"katasaya.html",context)

def del_quotes_ajax(request):
    if request.method == 'POST':
        id = request.get('id')
        kata_hapus = quotes.objects.get(pk=id)
        kata_hapus.delete()

        return HttpResponse(b"DIHAPUS", status=201)

    return HttpResponseNotFound()

def show_xml(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)



def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response


def edit_buku(request, id):
    # Get buku berdasarkan ID
    buku = Buku.objects.get(pk = id)

    # Set buku sebagai instance dari form
    form = BukuForm(request.POST or None, instance=buku)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_buku.html", context)


def delete_buku(request, id):
    # Get data berdasarkan ID
    buku = Buku.objects.get(pk = id)
    # Hapus data
    buku.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))


def show_preview(request, id):
    buku = Buku.objects.get(pk = id)
    context = {
        'buku': buku,
    }
    return render(request, "preview.html", context)