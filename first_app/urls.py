from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    path('calculadora', views.calculadora, name='calculadora')
]
