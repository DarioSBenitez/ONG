"""ong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Agreagar un import:  from my_app import views
    2. Agregar una URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL a urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Importar la funcion include(): from django.urls import include, path
    2. agregar una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ong.views import inicio, saludo2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina1/', inicio.saludo1, name='home'),
    path('pagina2/', saludo2)
   
]
