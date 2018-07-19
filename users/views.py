from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from users import models, serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class =  serializers.UserSerializer

