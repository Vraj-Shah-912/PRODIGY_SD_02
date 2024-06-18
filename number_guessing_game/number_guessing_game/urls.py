# number_guessing_game/urls.py
from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
