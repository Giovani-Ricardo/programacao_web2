import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','primeiro_projeto.settings')

import django
django.setup()

import random
from  first_app.models import Subject,Webpage,AcessRecord
from faker import Faker

if __name__ == '__main__':
    lista = AcessRecord.objects.all()
    print(lista.__len__())