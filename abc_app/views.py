from django.shortcuts import render
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
