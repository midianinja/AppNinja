from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Ninja, PerfilNinja, Causa, Interesse, Habilidade


class NinjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ninja
        fields = '__all__'


class PerfilNinjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilNinja
        fields = '__all__'


class HabilidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habilidade
        fields = '__all__'


class InteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesse
        fields = '__all__'


class CausaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Causa
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    def create(self, data):
        if data.get('password'):
            data['password'] = make_password(data['password'])
            data['is_active'] = False
        return super().create(data)

    # ninja = NinjaSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_superuser', 'groups')  # , 'ninja')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}
