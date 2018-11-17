from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, data):
        if data.get('password'):
            data['password'] = make_password(data['password'])
        return super().create(data)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_superuser', 'groups')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}
