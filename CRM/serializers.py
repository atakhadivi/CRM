# serializers.py

from followups.models import FollowUp
from companies.models import Contact
from rest_framework import serializers
from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'category')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'company')


class FollowUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = FollowUp
        fields = ('id', 'contact', 'company', 'date', 'notes')
