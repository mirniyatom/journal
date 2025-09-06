from django.shortcuts import render, redirect
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

def index(request):
    li_elements = ''
    for m in mainmenu_dict:
        redirect_path = reverse('main_menu', args=[m,])
        li_elements += f'<li> <a href="{redirect_path}">{m.title()}</a></li>'
    response = f"""
            <ul style="list-style-type: none; display: flex; gap: 15px; padding: 0; margin: 0;">
                {li_elements}
            </ul>"""
    return HttpResponse(response)


def get_mainmenu(request, main_menu):
    desc = mainmenu_dict.get(main_menu)
    if desc:
        return HttpResponse(desc)
    else:
        return HttpResponseNotFound(f'{main_menu} menu not found')