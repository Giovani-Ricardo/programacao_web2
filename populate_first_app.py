import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','primeiro_projeto.settings')

import django
django.setup()

import random
from  first_app.models import Subject,Webpage,AcessRecord
from faker import Faker

fakegen = Faker()

def populate_subject():
    subjects = ["Pesquisa", "Tecnologia", "Rede Social", "Esporte", "Streaming"]
    for subject in subjects:
        record = Subject(name=subject)
        record.save()


def populate_webpage(n=5):
    subjects = Subject.objects.all()

    for i in range(n):
        url = fakegen.url()
        # Pegando nome do site
        url_pieces = url.split('.')
        name = ''
        if(url_pieces.__len__() >= 3):
            name = url_pieces[1].capitalize()
        else:
            piece = url_pieces[0].split('//')
            name = piece[1].capitalize()
        
        # Pega um subject aleátorio para associar ao novo registro de webpage
        subject = subjects[random.randint(0,4)]
    
        # Verificar ordem dos parametros
        record = Webpage(url=url,name=name,subject=subject)
        record.save()


def populate_acess_record(n=5):
    webpages = Webpage.objects.all()

    for i in range(n):
        data = fakegen.date()

        # Pegando uma webpage aleatóriamente para associar ao novo registro de Ace
        webpage = webpages[random.randint(0,webpages.__len__() - 1)]
        record = AcessRecord(name=webpage,date=data)
        record.save()


if __name__ == '__main__':
    print("")
    #populate_subject()
    #populate_webpage(20)
    #populate_acess_record(100)
    print('')
