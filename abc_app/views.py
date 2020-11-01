from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Case, CaseLink, Incident
from .serializers import AccountSerializer, CaseSerializer, CaseLinkSerializer, IncidentSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CaseView(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseLinkView(viewsets.ModelViewSet):
    queryset = CaseLink.objects.all()
    serializer_class = CaseLinkSerializer

class IncidentView(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
