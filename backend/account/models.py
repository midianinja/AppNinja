# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, first_name, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_superuser(self, email, first_name, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, first_name, password, **extra_fields)

class User(AbstractUser):

    username = None
    recover = models.BooleanField(default=False)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()


# Create your models here.


class Habilidade(models.Model):

    descricao = models.CharField(unique=True, max_length=500)

    def __str__(self):
        return self.descricao

class Interesse(models.Model):

    descricao = models.CharField(unique=True, max_length=500)

    def __str__(self):
        return self.descricao

class Causa(models.Model):

    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao

class Pais(models.Model):

    nome = models.CharField(unique=True, max_length=500)

class Estado(models.Model):

    nome = models.CharField(unique=True, max_length=500)
    sigla_uf = models.CharField(unique=True, null=True, max_length=500)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

class Cidade(models.Model):

    nome = models.CharField(unique=True, max_length=500)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

class PerfilNinja(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    interesses = models.ManyToManyField(Interesse)
    causas = models.ManyToManyField(Causa)
    habilidades = models.ManyToManyField(Habilidade)

    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    telefone = models.CharField(max_length=500)
    data_nascimento = models.DateField()
    twitter = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    telegram = models.CharField(max_length=500)
    profissao = models.CharField(max_length=500)
    bio = models.TextField('bio', max_length=500)

    GENDER_CHOICES = (
        (0, 'Masculino'),
        (1, 'Feminino'),
        (2, 'Prefiro não declarar'),
    )
    genero = models.IntegerField(choices=GENDER_CHOICES, null=True)

    ORIENT_SEX_CHOICES = (
        (0, 'Heterossexual'),
        (1, 'Homossexual'),
        (2, 'Bissexual'),
        (3, 'Pansexual'),
        (4, 'Assexual'),
        (5, 'Fluido'),
        (6, 'Prefiro não declarar')
    )
    orientacao_sexual = models.IntegerField(choices=ORIENT_SEX_CHOICES, null=True)

    ID_GEN_CHOICES = (
        (0, 'Cisgênero'),
        (1, 'Transgênero'),
        (2, 'Neutro ou Não-binario'),
        (3, 'Prefiro não declarar')
    )
    identidade_genero = models.IntegerField(choices=ID_GEN_CHOICES, null=True)

    ETNIA_CHOICES = (
        (0, 'Negra'),
        (1, 'Indígena'),
        (2, 'Asiática'),
        (3, 'Caucasiana'),
        (4, 'Mestiça'),
        (5, 'Outra')
    )
    etnia = models.IntegerField(choices=ETNIA_CHOICES, null=True)

class Ninja(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #mapeamento da tabela Ninja, tamanho dos campos não são reais/oficiais
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=10)
    pais = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    dataNascimento = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)
    etnia = models.CharField(max_length=10)
    orientacao = models.CharField(max_length=10)
    identidade = models.CharField(max_length=10)
    twitter = models.CharField(max_length=10)
    facebook = models.CharField(max_length=10)
    instagram = models.CharField(max_length=10)
    telegram = models.CharField(max_length=10)
    causas = models.CharField(max_length=10)
    bio = models.CharField(max_length=10)
    profissao = models.CharField(max_length=10)
