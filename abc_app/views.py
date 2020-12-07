from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from .models import Account, Case, CaseLink, Incident
from .serializers import LoginSerializer, AccountSerializer, CaseSerializer, CaseLinkSerializer, IncidentSerializer

import pdb

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)

class UserCreateView(CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'user': serializer.data,
            'status': status_code,
            'message': "Hooray you made it!",
        }
        return Response(response, status_code)

class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        status_code = status.HTTP_200_OK
        response = {
            'token': serializer.data['token'], 
            'email': serializer.data['email'],
        }
        return Response(response, status_code)

class CaseView(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseLinkView(ListCreateAPIView):
    queryset = CaseLink.objects.all()
    serializer_class = CaseLinkSerializer

    def post(self, request):
        data = { 'case_id': request.data['case'], 'account_id': request.user.id }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'user': serializer.data,
            'status': status_code,
            'message': "Hooray you made it!",
        }
        return Response(response, status_code)

class IncidentView(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer