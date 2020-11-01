from rest_framework import serializers
from .models import Account, Case, CaseLink, Incident

class IncidentObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'antecedent', 'behavior', 'consequence', 'date', 'time']

class CaseObjectSerializer(serializers.ModelSerializer):
    incidents = IncidentObjectSerializer(many=True)
    class Meta:
        model = Case
        fields = ['id', 'name', 'dob', 'incidents']

class AccountObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email']

class AccountSerializer(serializers.ModelSerializer):
    cases = CaseObjectSerializer(many=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'cases']

class CaseSerializer(serializers.ModelSerializer):
    accounts = AccountObjectSerializer(many=True)
    incidents = IncidentObjectSerializer(many=True)
    class Meta:
        model = Case
        fields = ['id', 'name', 'dob', 'accounts', 'incidents']
    
class CaseLinkSerializer(serializers.ModelSerializer):
    account = serializers.StringRelatedField(many=False)
    case = serializers.StringRelatedField(many=False)
    class Meta:
        model = CaseLink
        fields = ['id', 'account', 'case']

class IncidentSerializer(serializers.ModelSerializer):
    case = serializers.StringRelatedField(many=False)
    class Meta:
        model = Incident
        fields = ['id', 'antecedent', 'behavior', 'consequence', 'date', 'time', 'case']