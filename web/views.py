from django.http import HttpResponse
from django.shortcuts import render, redirect

from mysite import settings
from web.models import Publication, Heroes


def index(request):
    return render(request, 'main.html')


def post(request):
    if request.method == 'POST':  # публикация в раздел галерея
        title = request.POST.get('title')
        text = request.POST.get('text')
        password = request.POST.get('password')
        if password != settings.SECRET_KEY:
            return render(request, 'post.html', {
                'error': 'Пароль неверный'
            })
        if title and text:
            Publication.objects.create(title=title, text=text)
            return redirect('/gallery')
        else:
            return render(request, 'post.html', {
                'error': 'title и text должны быть не пустыми'
            })
    return render(request, 'post.html')


def gallery(request):
    publications_sorted = Publication.objects.order_by('-date')
    return render(request, 'publications.html', {
        'publications': publications_sorted
    })


def publication(request, pub_id):
    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DousNotExist:
        return redirect('/')
    return render(request, 'publication.html', {
        'publication': publication
    })


def post_2(request):  # публикация в раздел люди
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        password = request.POST.get('password')
        if password != settings.SECRET_KEY:
            return render(request, 'post.html', {
                'error': 'Пароль неверный'
            })
        if title and text:
            Heroes.objects.create(title=title, text=text)
            return redirect('/heroes')
        else:
            return render(request, 'post.html', {
                'error': 'title и text должны быть не пустыми'
            })
    return render(request, 'post_2.html')


def heroes(request):
    heroes_sorted = Heroes.objects.order_by('-date')
    return render(request, 'heroes.html', {
        'heroes': heroes_sorted
    })


def hero(request, pub_id):
    try:
        hero = Heroes.objects.get(id=pub_id)
    except Heroes.DousNotExist:
        return redirect('/')
    return render(request, 'hero.html', {
        'hero': hero
    })


def art(request):
    return render(request, 'art.html')  # не редактировала


def aboutwar(request):
    return render(request, 'aboutwar.html')  # не редактировала


def films(request):
    return render(request, 'films.html')  # не редактировала


def excursions(request):
    return render(request, 'excursions.html')  # не редактировала


def songs(request):
    return render(request, 'songs.html')  # не редактировала


def contacts(request):
    return render(request, 'contacts.html')


def status(request):
    return HttpResponse("Status OK")
