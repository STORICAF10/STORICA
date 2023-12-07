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
from django.core.files.storage.filesystem import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist


def get_buku_json(request):
    buku = Buku.objects.all().order_by("jumlah_review")
    return HttpResponse(serializers.serialize("json", buku))


def get_bukukreasi_json(request):
    bukukreasi = Buku.objects.all().order_by("jumlah_review")
    return HttpResponse(serializers.serialize("json", bukukreasi))


def show_semua(request):
    karya_pengguna = (
        BukuKreasi.objects.all().order_by("jumlah_review").filter(is_published=True)
    )
    bukus = Buku.objects.all().order_by("jumlah_review")

    context = {"bukus": bukus, "karya": karya_pengguna}
    return render(request, "semuabuku.html", context)


def show_main(request):
    karya_pengguna = (
        BukuKreasi.objects.all().order_by("jumlah_review").filter(is_published=True)
    )
    bukus = Buku.objects.all().order_by("jumlah_review")
    kata_bijak = quotes.objects.all()

    if "last_login" in request.COOKIES:
        if "last_login" in request.COOKIES:
            try:
                tingkatan = level.objects.get(user=request.user)
            except ObjectDoesNotExist:
                tingkatan = level(
                    user=request.user, level=0, buku_total=0, batas_atas=5, persen=0
                )
                tingkatan.save()

        context = {
            "persen": 100 * tingkatan.buku_total / tingkatan.batas_atas,
            "tingkatan": tingkatan,
            "kata_bijak": kata_bijak,
            "pengguna": request.user,
            "last_login": request.COOKIES["last_login"],
            "bukus": bukus,
            "karya": karya_pengguna,
        }
    else:
        context = {"kata_bijak": kata_bijak, "bukus": bukus, "karya": karya_pengguna}

    return render(request, "main.html", context)


@login_required(login_url="/login")
def create_buku(request):
    if request.method == "POST":
        form = BukuForm(request.POST, request.FILES)
        if form.is_valid():
            buku = form.save(commit=False)
            print(buku)
            buku.user = request.user
            buku.save()
            return HttpResponseRedirect(reverse("main:show_main"))

    else:
        form = BukuForm()

    context = {"form": form}
    return render(request, "create_buku.html", context)


def create_buku_baru(request):
    if request.method == "POST":
        print("\n Masuk bNag KE SAVE \n")
        form = BukuForm(request.POST, request.FILES)
        if form.is_valid():
            buku = form.save(commit=False)
            buku.user = request.user
            buku.save()
            return HttpResponseRedirect(
                reverse("main:autoSave", kwargs={"id_buku": buku.id})
            )

    else:
        form = BukuForm()

    context = {"form": form}
    return render(request, "create_buku_baru.html", context)


@csrf_exempt
def add_quotes_ajax(request):
    if request.method == "POST":
        kata = request.POST.get("quotes")
        user = request.user

        new_quotes = quotes(kata_kata=kata, user=user)
        new_quotes.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def filter_bintang_empat(request):
    karya_pengguna = (
        BukuKreasi.objects.all()
        .order_by("jumlah_review")
        .filter(is_published=True)
        .filter(rating__gt=4)
    )
    bukus = Buku.objects.all().order_by("jumlah_review").filter(rating__gt=4)

    if "last_login" in request.COOKIES:
        if hasattr(request, "level"):
            tingkatan = level.objects.get(user=request.user)
        context = {
            "persen": 100 * tingkatan.buku_total / tingkatan.batas_atas,
            "tingkatan": tingkatan,
            "pengguna": request.user,
            "last_login": request.COOKIES["last_login"],
            "bukus": bukus,
            "karya": karya_pengguna,
        }
    else:
        context = {"bukus": bukus, "karya": karya_pengguna}
    return render(request, "filterbintangempat.html", context)


def filter_bahasa_inggris(request):
    karya_pengguna = (
        BukuKreasi.objects.all()
        .order_by("jumlah_review")
        .filter(is_published=True)
        .filter(bahasa="eng")
    )
    bukus = Buku.objects.all().order_by("jumlah_review").filter(bahasa="eng")

    if "last_login" in request.COOKIES:
        if hasattr(request, "level"):
            tingkatan = level.objects.get(user=request.user)
        context = {
            "persen": 100 * tingkatan.buku_total / tingkatan.batas_atas,
            "tingkatan": tingkatan,
            "pengguna": request.user,
            "last_login": request.COOKIES["last_login"],
            "bukus": bukus,
            "karya": karya_pengguna,
        }
    else:
        context = {"bukus": bukus, "karya": karya_pengguna}
    return render(request, "filterbukuinggris.html", context)


def filter_buku_karya(request):
    karya_pengguna = (
        BukuKreasi.objects.all().order_by("jumlah_review").filter(is_published=True)
    )

    if "last_login" in request.COOKIES:
        if hasattr(request, "level"):
            tingkatan = level.objects.get(user=request.user)
        context = {
            "persen": 100 * tingkatan.buku_total / tingkatan.batas_atas,
            "tingkatan": tingkatan,
            "pengguna": request.user,
            "last_login": request.COOKIES["last_login"],
            "karya": karya_pengguna,
        }
    else:
        context = {"karya": karya_pengguna}
    return render(request, "filterbukuinggris.html", context)


@login_required(login_url="/login")
def show_my_quotes(request):
    kata_saya = quotes.objects.filter(user=request.user)

    context = {"kata_saya": kata_saya}

    return render(request, "katasaya.html", context)


def delete_quotes(request, id):
    katabijak = quotes.objects.get(pk=id)
    katabijak.delete()
    return HttpResponseRedirect(reverse("main:show_my_quotes"))


def show_xml(request):
    data = Buku.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_buku_json(request):
    data = Buku.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_buku_kreasi_json(request):
    data = BukuKreasi.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_quotes_json(request):
    data = BukuKreasi.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_profile_json(request):
    user = request.user
    data = profile.objects.filter(user=user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_level_json(request):
    user = request.user
    data = level.objects.filter(user=user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_my_quotes_json(request):
    user = request.user
    data = quotes.objects.filter(user=user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(
                request, "Sorry, incorrect username or password. Please try again."
            )
    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.delete_cookie("last_login")
    return response


def edit_buku(request, id):
    # Get buku berdasarkan ID
    buku = Buku.objects.get(pk=id)

    # Set buku sebagai instance dari form
    form = BukuForm(request.POST or None, instance=buku)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse("main:show_main"))

    context = {"form": form}
    return render(request, "edit_buku.html", context)


@login_required(login_url="/login")
def delete_buku(request, id):
    # Get data berdasarkan ID
    buku = Buku.objects.get(pk=id)
    # Hapus data
    buku.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse("main:show_main"))


def show_preview(request, id):
    buku = Buku.objects.get(pk=id)
    context = {
        "buku": buku,
    }
    return render(request, "preview_biasa.html", context)

def show_preview_kreasi(request, id):
    karya = BukuKreasi.objects.get(pk=id)
    context = {
        "karya": karya,
    }
    return render(request, "preview_kreasi.html", context)

def get_quotes_json(request):
    katabijak = quotes.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", katabijak))


def createIsiBuku(request):
    buku = BukuKreasi.objects.filter(user=request.user)
    form = BukuForm(request.POST, request.FILES)

    print("Masuk baNag okk createisibuku")
    if request.method == "POST":
        if form.is_valid():
            isi_buku = request.POST.get("isi_buku")
            if isi_buku != "":
                buku.isi_buku = isi_buku
                buku.is_published = False
                buku = form.save(commit=False)
                buku.save()
                print(buku.judul)
                form.save()
                return HttpResponseRedirect(
                    reverse("main:autoSave", kwargs={"id_buku": buku.id})
                )

            else:
                messages.info(request, "Field Cannot Empty")

    context = {"form": form, "buku": buku}
    return render(request, "create_isi_buku_baru.html", context)


def autoSave(request, id_buku):
    # print(id_buku)
    buku = BukuKreasi.objects.get(id=id_buku)
    print(buku)
    print("sini")

    if request.method == "POST":
        print("Masuk bsaNag")
        isi_buku = request.POST.get("isi_buku")
        buku.isi_buku = isi_buku
        buku.is_published = True
        buku.save()
        print(buku.isi_buku + " auto save uye")
        return HttpResponseRedirect(
            reverse("main:autoSave", kwargs={"id_buku": id_buku})
        )

    else:
        form = BukuForm()
        print("get")

    # print(form.isi_buku)
    context = {"form": form, "buku": buku}
    print(buku)
    return render(request, "create_isi_buku_continue.html", context)


def publish(request, id_buku):
    buku = BukuKreasi.objects.get(id=id_buku)
    print("masuk Publish")
    buku.is_published = True
    print(buku.is_published)
    buku.save()
    print(buku.isi_buku + " uye")
    return HttpResponseRedirect(reverse("main:show_main"))

    # print(form.isi_buku)
    context = {"form": form, "buku": buku}
    print(buku)
    return render(request, "create_isi_buku_continue.html", context)


def showCover(request):
    context = {}
    print("foto siap")
    if request.method == "POST":
        print("FGoto masuk")
        uploaded_file = request.FILE["document"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
    return HttpResponseRedirect(reverse("main:show_main"))
