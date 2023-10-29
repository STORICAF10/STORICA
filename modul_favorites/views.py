from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from main.models import Buku
from main.models import BukuKreasi

# Create your views here.
@login_required(login_url='/login')
def show_favorites(request):
    buku = request.user.buku_set.all()
    print(buku)
    context = {
        'karya': buku,
    }
    return render(request, "show_favorites.html", context)

@login_required(login_url='/login')
def add_favorites(request,id):
    buku = Buku.objects.get(pk = id)
    user = request.user
    buku.buku_favorites.add(user)
    buku.save()
    return HttpResponseRedirect(reverse('modul_favorites:show_favorites'))

@login_required(login_url='/login')
def remove_favorites(request,id):
    buku = Buku.objects.get(pk = id)
    user = request.user
    buku.buku_favorites.remove(user)
    buku.save()
    return HttpResponseRedirect(reverse('modul_favorites:show_favorites'))

@login_required
def toggle_favorites(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        action = request.POST.get('action')
        buku = Buku.objects.get(pk=id)
        user = request.user

        if action == 'add':
            buku.buku_favorites.add(user)
            buku.save()
            return JsonResponse({'status': 'added'})
        elif action == 'remove':
            buku.buku_favorites.remove(user)
            buku.save()
            return JsonResponse({'status': 'removed'})

    return JsonResponse({'status': 'error'})
