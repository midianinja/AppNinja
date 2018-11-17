# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView as BaseAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
from django.conf import settings
from .models import User
from .serializers import UserSerializer

class APIView(BaseAPIView):
    def has_perm_on_object(self, user, obj, perm):
        return user.is_superuser or user.id == obj.id

class UserList(APIView):

    """
    List all users or create a new one
    """
    permission_classes = [AllowAny]
    # permission_classes = [permissions.DjangoModelPermissions]

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
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()
        if not request.user.is_superuser or data.get('user') is None:
            data['user'] = request.user.id
        if data.get('is_superuser') and not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

