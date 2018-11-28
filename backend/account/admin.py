# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Habilidade, Interesse, Causa, Pais, Estado, Cidade, PerfilNinja, Ninja, User

# Register your models here.

admin.site.register(Habilidade)
admin.site.register(Interesse)
admin.site.register(Causa)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(PerfilNinja)
admin.site.register(Ninja)
admin.site.register(User)

