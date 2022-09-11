# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from datetime import date
from django.shortcuts import render

from . import forms
from .forms import FormWebpage,FormAcessRecord
from .models import Subject,Webpage,AcessRecord


# Create your views here.
def index(request):
    webpage_form = forms.FormWebpage()
    data_atual = date.today()
    # acess_record_form = form.FormAcessrecord()

    my_dict = {
        'insert_me': "Hello, my name is Giovani!",
        'webpage_form': webpage_form,
        'data_atual':data_atual
        # 'acess_record_form' = acess_record_form
    }

    if request.method == 'POST':
        webpage_form = forms.FormWebpage(request.POST)
        if webpage_form.is_valid():
            webpage_form.save(commit=True)
            return index(request)
            # acess_record_form = form.FormAcessrecord()
        else:
            print('ERRO FORM INVALID')

    return render(request, 'primeiro_projeto/index.html', context=my_dict)


def calculadora(resquest):
    return render(resquest, 'primeiro_projeto/calculadora.html')


def londrina(request):
    return render(request, 'primeiro_projeto/londrina.html')


def help(request):
    my_dict = {'insert_me' : 'Página de ajuda'}
    return render(request, 'primeiro_projeto/help.html', context=my_dict)


def paginas(request):
    paginas = Webpage.objects.all()
    context = {
        'paginas': paginas
    }
    return render(request, 'primeiro_projeto/paginas.html', context)


def registros_acesso(request):
    acessos = AcessRecord.objects.all()
    context = {
        'acessos': acessos
    }
    return render(request, 'primeiro_projeto/registros_acesso.html', context)