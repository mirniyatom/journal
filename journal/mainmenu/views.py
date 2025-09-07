from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


mainmenu_dict = {
    'about': 'Jurnal haqida',
    'conference' : 'Konfirensiyalar haqida',
    'forauthors' : 'Avtorlar uchun',
    'archive' : 'Chop qilingan nomerlar',
    'subscription': 'Jurnalga obuna bolish',
    'news': 'Yangiliklar',
    'contacts': 'Boglanish uchun kontaktlar pochta va adress',
    'login': 'Avtorizatsiya yoki registratsiya'

}

def index(request):
    context = {
        'title': 'Bosh menyu',
        'content' : 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/index.html', context)

def about(request):
    context = {
        'title': 'Bosh menyu',
        'content' : 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/about.html', context)

def conference(request):
    context = {
        'title': 'Bosh menyu',
        'content' : 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/conference.html', context)

def forauthors(request):
    context = {
        'title': 'Bosh menyu',
        'content': 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/forauthors.html', context)

def archive(request):
    context = {
        'title': 'Bosh menyu',
        'content': 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/archive.html', context)

def subscription(request):
    context = {
        'title': 'Bosh menyu',
        'content': 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/subscription.html', context)


def news(request):
    context = {
        'title': 'Bosh menyu',
        'content': 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/news.html', context)


def contacts(request):
    context = {
        'title': 'Bosh menyu',
        'content': 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/contacts.html', context)

def login(request):
    context = {
        'title': 'Bosh menyu',
        'content': 'Zarracha jurnali'
    }
    return render(request, 'mainmenu/login.html', context)