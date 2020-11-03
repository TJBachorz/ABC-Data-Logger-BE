from rest_framework import serializers
from .models import Account, Case, CaseLink, Incident

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email']

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'antecedent', 'behavior', 'consequence', 'date', 'time', 'case']

class CaseObjectSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True)
    incidents = IncidentSerializer(many=True)
    class Meta:
        model = Case
        fields = ['id', 'name', 'dob', 'accounts', 'incidents']

class CaseObjectForAccountSerializer(serializers.ModelSerializer):
    incidents = IncidentSerializer(many=True)
    class Meta:
        model = Case
        fields = ['id', 'name', 'dob', 'incidents']

class AccountObjectSerializer(serializers.ModelSerializer):
    cases = CaseObjectForAccountSerializer(many=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'cases']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['id', 'name', 'dob']  
    
class CaseLinkSerializer(serializers.ModelSerializer):
    account = serializers.StringRelatedField(many=False)
    case = serializers.StringRelatedField(many=False)
    class Meta:
        model = CaseLink
        fields = ['id', 'account', 'case']
