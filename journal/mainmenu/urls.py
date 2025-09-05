from django.urls import path
from . import views

urlpatterns = [
    path('<main_menu>/', views.get_mainmenu, name='main_menu'),
]