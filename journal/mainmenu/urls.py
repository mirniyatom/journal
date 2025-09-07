from django.urls import path
from . import views


app_name = 'mainmenu'
urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name="about"),
    path("conferences/", views.conference, name="conference"),
    path("forauthors/", views.forauthors, name="forauthors"),
    path("archive/", views.archive, name="archive"),
    path("subscription/", views.subscription, name="subscription"),
    path("news/", views.news, name="news"),
    path("contacts/", views.contacts, name="contacts"),
    path("login/", views.login, name="login"),

]