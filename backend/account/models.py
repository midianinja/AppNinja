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
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    GENDER_CHOICES = (
        (0, 'Masculino'),
        (1, 'Feminino'),
        (2, 'Prefiro não declarar'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)

    ORIENT_SEX_CHOICES = (
        (0, 'Heterossexual'),
        (1, 'Homossexual'),
        (2, 'Bissexual'),
        (3, 'Pansexual'),
        (4, 'Assexual'),
        (5, 'Fluido'),
        (6, 'Prefiro não declarar')
    )
    orient_sex = models.IntegerField(choices=ORIENT_SEX_CHOICES, null=True)

    ID_GEN_CHOICES = (
        (0, 'Cisgênero'),
        (1, 'Transgênero'),
        (2, 'Neutro ou Não-binario'),
        (3, 'Prefiro não declarar')
    )
    ident_genero = models.IntegerField(choices=ID_GEN_CHOICES, null=True)

    ETNIA_CHOICES = (
        (0, 'Negra'),
        (1, 'Indígena'),
        (2, 'Asiática'),
        (3, 'Caucasiana'),
        (4, 'Mestiça'),
        (5, 'Outra')
    )
    etnia = models.IntegerField(choices=ETNIA_CHOICES, null=True)

# Create your models here.
