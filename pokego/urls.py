"""pokego URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from usuario import views as usuario_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('liga.urls')),
    path('', include('participar.urls')),
    path('registrar/', usuario_views.registrar, name="registrar"),
    path('perfil/', usuario_views.profile, name="perfil"),
    path('entrar/', auth_views.LoginView.as_view(template_name="usuario/entrar.html"), name="entrar"),
    path('salir/', auth_views.LogoutView.as_view(template_name="usuario/salir.html"), name="salir"),
]
