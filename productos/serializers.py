from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Escaneos,Categoria,Local,Permiso
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields='__all__'
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Local
        fields='__all__'
class EscaneosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Escaneos
        fields='__all__'
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Permiso
        fields='__all__'