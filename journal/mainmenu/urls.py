from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<main_menu>/', views.get_mainmenu, name='main_menu'),
]