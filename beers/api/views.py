from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.base import View
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from beers.api.serializers import BeerSerializer, CompanySerializer, UserSerializer, RecetaSerializer
from beers.models import Beer, Company, Receta


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListAPI(View):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        serialized_users = serializer.data #lista de diccionarios
        renderer = JSONRenderer()
        json_users = renderer.render(serialized_users) #lisa de diccionarios -> JSON
        return HttpResponse(json_users)

