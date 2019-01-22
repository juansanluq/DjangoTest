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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','last_login','username','first_name','email','date_joined','last_name')

class RecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receta
        fields = ('id','name','tiempo_preparacion','created_by_id','pdf')
