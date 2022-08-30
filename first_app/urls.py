from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    path('calculadora', views.calculadora, name='calculadora')
]
