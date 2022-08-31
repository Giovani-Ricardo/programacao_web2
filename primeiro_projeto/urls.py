"""primeiro_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('londrina', views.londrina, name='londrina'),
    path('paginas', views.paginas, name='paginas'),
    path('registros_acesso', views.registros_acesso, name='registros_acesso'),
    url(r'^admin/', admin.site.urls),
    path('first_app/', include('first_app.urls'))
]
