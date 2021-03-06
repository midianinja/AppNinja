# Generated by Django 2.1.3 on 2018-11-24 14:03

from django.db import migrations
from account.models import Causa, Interesse, Habilidade

def load_initial_db(apps, schema_editor):
    c = Causa()
    c.descricao = 'Causa X'
    c.save()

    i = Interesse()
    i.descricao = 'Interesse Y'
    i.save()

    h = Habilidade()
    h.descricao = 'Habilidade Z'
    h.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_db)
    ]
