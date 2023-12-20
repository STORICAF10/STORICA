from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


from main.models import Buku
from main.models import BukuKreasi

# Create your views here.
@login_required(login_url='/login')
def show_favorites(request):
    user = request.user
    buku = request.user.buku_set.all()
    print(buku)
    context = {
        'karya': buku,
    }
    return render(request, "show_favorites.html", context)


@login_required(login_url='/login')
def add_favorites(request,id):
    user = request.user
    buku = Buku.objects.get(pk = id)
    buku.buku_favorites.add(user)
    buku.save()
    return HttpResponseRedirect(reverse('modul_favorites:show_favorites'))


@login_required(login_url='/login')
def remove_favorites(request,id):
    user = request.user
    buku = Buku.objects.get(pk = id)
    buku.buku_favorites.remove(user)
    buku.save()
    return HttpResponseRedirect(reverse('modul_favorites:show_favorites'))

# @login_required(login_url='/login')
@api_view(['POST'])
def add_to_favorites(request,nama,id):
    buku = Buku.objects.get(pk = id)
    user = User.objects.get(username = nama)
    buku.buku_favorites.add(user)
    buku.save()
    return Response({'message': 'Book added to favorites'}, status=200)


# @login_required(login_url='/login')
@api_view(['POST'])
def remove_from_favorites(request,nama,id):
    buku = Buku.objects.get(pk = id)
    user = User.objects.get(username = nama)
    buku.buku_favorites.remove(user)
    buku.save()
    return Response({'message': 'Book removed from favorites'}, status=200)


def check_favorite(request, nama, id):
    user = User.objects.get(username = nama)
    buku = Buku.objects.get(pk=id)
    is_favorite = buku.buku_favorites.filter(pk=user.pk).exists()
    return JsonResponse({'is_favorite': is_favorite})

def show_favorites_json(request, nama):
    user = User.objects.get(username = nama)
    buku_queryset = Buku.objects.filter(buku_favorites=user)
    buku_json = serializers.serialize('json', buku_queryset)
    return HttpResponse(buku_json, content_type='application/json')