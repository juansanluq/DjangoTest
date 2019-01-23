from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.base import View
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from beers.api.serializers import BeerSerializer, CompanySerializer, UserSerializer, RecetaSerializer
from beers.models import Beer, Company, Receta
from django.shortcuts import get_object_or_404


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListAPI(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user,many=False)
        return Response(serializer.data)




