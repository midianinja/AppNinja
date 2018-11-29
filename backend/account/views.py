# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView as BaseAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.conf import settings
from .models import User, Ninja, Habilidade, Causa, Interesse, PerfilNinja, Cidade
from .serializers import UserSerializer, HabilidadeSerializer, CausaSerializer, InteresseSerializer, PerfilNinjaSerializer
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json

class APIView(BaseAPIView):
    def has_perm_on_object(self, user, obj, perm):
        return user.is_superuser or user.id == obj.id

class UserList(APIView):

    """
    List all users or create a new one
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        users = User.objects
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            # Maybe there should be a 'view_user' permission, but this is on django.contrib.auth.
            # By now, let's use change_user permission, it's harmless by now, since these permissions
            # are always the same for all current roles
            if not request.user.is_superuser:
                Permission.objects.get(group__user=request.user, codename='change_user')
        except Permission.DoesNotExist:
            users = users.filter(id=request.user.id)
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()
        if not request.user.is_superuser or data.get('user') is None:
            data['user'] = request.user.id

        # if data.get('is_superuser') and not request.user.is_superuser:
        #     return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(data=data)
        # this checks if email is already in DB
        if serializer.is_valid():
            # caso o usuário não exista
            serializer.save()
            user = User.objects.get(email=data['email'])
            if self.envia_email_confirmacao(user):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            user = User.objects.get(email=data['email'])

            # caso o usuário já exista porém esteja inativo
            # contempla o caso do usuário carregado a partir dos cadastros da midia ninja

            if not user.is_active:
                user.password = make_password(serializer.data['password'])
                user.save()

                if self.envia_email_confirmacao(user):
                    return Response(serializer.data, status=status.HTTP_200_OK)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def envia_email_confirmacao(self, user):

        link = 'http://127.0.0.1:8000/api/account/users/confirm/{ID}/{TOKEN}'
        link = link.format(ID=user.id, TOKEN=Token.objects.get_or_create(user=user)[0].pk)

        msg = 'Clique em {LINK} para confirmar seu email'.format(LINK=link)

        return send_mail(
            'Confirmação de email',
            msg,
            'appninjamailer@gmail.com',
            [user.email],
            fail_silently=False,
        )

    @csrf_exempt
    def send_recover_password(request):
        # data = request.data.copy()
        data = request.POST

        if 'email' in data.keys():
            email = data['email']
            user = User.objects.get(email=email)
            if user:
                user.recover = True

                user.save()

                link = 'http://127.0.0.1:8000/api/account/users/recover/{ID}/{TOKEN}'
                link = link.format(ID=user.id, TOKEN=Token.objects.get_or_create(user=user)[0].pk)

                # TODO: como escrever um link que abra o aplicativo?
                msg = 'Clique em {LINK} para iniciar o processo de recuperação de senha'.format(LINK=link)

                if send_mail(
                    'Recuperação de senha',
                    msg,
                    'appninjamailer@gmail.com',
                    [user.email],
                    fail_silently=False,
                ):
                    return HttpResponse(status=status.HTTP_200_OK)

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def recover_password(request, user_id, token):
        user = User.objects.get(id=user_id)
        data = request.POST
        if user.recover == True and token == Token.objects.get(user=user).key:

            user.recover = False
            user.password = make_password(data['password'])
            user.is_active = True
            user.save()

            send_mail(
                'Confirmação de alteração de senha',
                'Sua senha foi alterada com sucesso',
                'appninjamailer@gmail.com',
                [user.email],
                fail_silently=False,
            )
            return HttpResponse(status=status.HTTP_200_OK)

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def email_verification(request, user_id, token):
        user = User.objects.get(id=user_id)
        if user.is_active == False and token == Token.objects.get(user=user).key:
            user.is_active = True
            user.save()

            send_mail(
                'Confirmação de email',
                'Seu email {EMAIL} foi verificado com sucesso'.format(EMAIL=user.email),
                'appninjamailer@gmail.com',
                [user.email],
                fail_silently=False,
            )

    def list_skills(request):
        skills = Habilidade.objects.all()
        serializer = HabilidadeSerializer(skills, many=True)
        return JsonResponse(serializer.data, safe=False)

    def list_causes(request):
        causas = Causa.objects.all()
        serializer = CausaSerializer(causas, many=True)
        return JsonResponse(serializer.data, safe=False)

    def list_interests(request):
        interests = Interesse.objects.all()
        serializer = InteresseSerializer(interests, many=True)
        return JsonResponse(serializer.data, safe=False)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        # Maybe there should be a 'view_user' permission, but this is on django.contrib.auth.
        # By now, let's use change_user permission, it's harmless by now, since these permissions
        # are always the same for all current roles
        if not self.has_perm_on_object(request.user, user, 'change_user'):
            # Using 404 instead of 403 for privacy
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = request.data.copy()
        if not request.user.is_superuser:
            data['user'] = request.user.id
        user = self.get_object(pk)
        if (user.is_superuser or data.get('is_superuser')) and not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if not self.has_perm_on_object(request.user, user, 'change_user'):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if not self.has_perm_on_object(request.user, user, 'delete_user'):
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserMe(UserDetail):

    def get(self, request, format=None):
        return super().get(request, request
 .user.id, format)
    def put(self, request, format=None):
        return super().put(request, request.user.id, format)
    def delete(self, request, format=None):
        return super().delete(request, request.user.id, format)

class AuthLogin(BaseAPIView):

    permission_classes = [AllowAny]
    def post(self, request, format=None):
        for field in ('email', 'password'):
            if not request.data.get(field):
                return Response("E-mail, password are required", status=status.HTTP_401_UNAUTHORIZED)            
        try:
            user = User.objects.get(email=request.data['email'])
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(request.data['password']):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        (token, created) = Token.objects.get_or_create(user=user)
        return Response({ 'data': {'token': token.key }})


class AuthLogout(BaseAPIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Cadastro(BaseAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        data = request.data

        perfil_ninja = PerfilNinja()

        perfil_ninja.user = request.user

        # lembrando que devem ser valores inteiros correspondente a etnia/orientacao/ident em questao
        perfil_ninja.etnia = data['etnia']
        perfil_ninja.orientacao_sexual = data['orientacao'] # semelhante a etnia
        perfil_ninja.identidade_genero = data['identidade'] # semelhante a etnia

        for causa in data['causas']:
            c = Causa.objects.get(id=causa)
            perfil_ninja.causas.add(c)

        for habilidade in data['habilidades']:
            h = Habilidade.objects.get(id=habilidade)
            perfil_ninja.habilidades.add(h)

        for interesse in data['interesses']:
            i = Interesse.objects.get(id=interesse)
            perfil_ninja.interesses.add(i)

        perfil_ninja.twitter = data['twitter']
        perfil_ninja.telefone = data['telefone']
        perfil_ninja.cidade = Cidade.objects.get(nome=data['cidade'])
        perfil_ninja.facebook = data['facebook']
        perfil_ninja.instagram = data['instagram']
        perfil_ninja.bio = data['bio']
        perfil_ninja.profissao = data['profissao']
        perfil_ninja.data_nascimento = data['dataNascimento'],

        # ninja = Ninja(user = request.user,
        #     nome=data['nome'],
        #     cidade=data['cidade'],
        #     estado=data['estado'],
        #     pais=data['nome'],
        #     telefone=data['telefone'],
        #     dataNascimento=data['dataNascimento'],
        #     etnia=data['etnia'],
        #     orientacao=data['orientacao'],
        #     identidade=data['identidade'],
        #     twitter=data['twitter'],
        #     facebook=data['facebook'],
        #     instagram=data['instagram'],
        #     causas=data['causas'],
        #     bio=data['bio'],
        #     profissao=data['profissao']
        # )

        perfil_ninja.save()

        return HttpResponse(status=status.HTTP_200_OK)

    def get(self, request, format=None):

        user = request.user
        try:
            perfil_ninja = user.perfilninja
            serializer = PerfilNinjaSerializer(perfil_ninja)

            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return HttpResponse(status.HTTP_204_NO_CONTENT)

        #elif request.method == 'GET':
            #return HttpResponse(json.dumps(data),content_type='application/json')

        #return HttpResponse(json.dumps(data),content_type='application/json')