from django.urls import path
from . import views

urlpatterns = [
    path('participar/', views.participar, name='participar-home'),
]