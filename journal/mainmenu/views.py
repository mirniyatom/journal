from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


mainmenu_dict = {
    'main' : 'Bu yerda bosh menyu',
    'about': 'Jurnal haqida',
    'conference' : 'Konfirensiyalar haqida',
    'forauthors' : 'Avtorlar uchun',
    'archive' : 'Chop qilingan nomerlar',
    'subscription': 'Jurnalga obuna bolish',
    'news': 'Yangiliklar',
    'contacts': 'Boglanish uchun kontaktlar pochta va adress',
    'login': 'Avtorizatsiya yoki registratsiya'

}

def get_mainmenu(request, main_menu):
    desc = mainmenu_dict.get(main_menu)
    if desc:
        return HttpResponse(desc)
    else:
        return HttpResponseNotFound(f'{main_menu} menu not found')