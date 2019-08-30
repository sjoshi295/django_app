from rest_framework import serializers
from banks.models import BankName, BankData
from django.contrib.auth.models import User


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankName
        fields = '__all__'


class BankBranchSerializer(serializers.ModelSerializer):
    b_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BankData
        fields = '__all__'
        depth = 2


class UserSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']
            
        