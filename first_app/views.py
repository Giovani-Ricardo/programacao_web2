# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello, my name is Giovani!"}
    return render(request, 'primeiro_projeto/index.html', context=my_dict)


def calculadora(resquest):
    return render(resquest, 'primeiro_projeto/calculadora.html')


def londrina(request):
    return render(request, 'primeiro_projeto/londrina.html')


def help(request):
    my_dict = {'insert_me' : 'Página de ajuda'}
    return render(request, 'primeiro_projeto/help.html', context=my_dict)