from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from main.models import profile
import json
from django.db.utils import IntegrityError
from main.models import *

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
    
        if user.is_active:
            auth_login(request, user)
            try:
                data = profile.objects.get(user=user)
            except:
                data = profile(user=user,gambar="")
                data.save()
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                 "gambar": data.gambar
                
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

@csrf_exempt
def app_register(request):
    try:
       
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        print(username)
        print(password)
        print(confirm)

        if password != confirm:
            return JsonResponse({'status': 'failed', 'message': 'Password tidak sesuai'})

        new_user = User.objects.create_user(username = username, password = password)
        new_user.save()
        return JsonResponse({"status": "success","username":username,}, status=200)
    except IntegrityError:
        return JsonResponse({"status": "error", 'message':'Username sudah digunakan.'}, status=401)
    except:
        return JsonResponse({"status": "error", 'message':'Terjadi error, pastikan jumlah karakter tidak lebih dari 150 dan hanya mengandung angka dan huruf.'}, status=401)
