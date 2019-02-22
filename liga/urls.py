from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='liga-home'),
    path('reglas/', views.reglas, name='reglas-home'),
    path('lista/', views.lista, name='lista-home'),
    path('buscar/', views.buscar, name='buscar-home'),
]
