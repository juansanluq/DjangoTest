from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from django.contrib.auth import models

from beers.models import Beer, Company, Receta


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ('name','abv','color','is_filtered','image')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','tax_number')

"""class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','last_login','username','first_name','email','date_joined','last_name')"""

class RecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receta
        fields = ('id','name','tiempo_preparacion','created_by_id','pdf')


#Serializador de usuarios
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    #password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos validated_data que contiene valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto User
        """
        instance = User()
        return self.update(instance,validated_data)


    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos del diccionario validated_data
        que contiene valores desereializados
        :param instance: objeto User a actualizar
        :param validated_data: diccionario con nuevos valores para el User
        :return: objeto User actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
