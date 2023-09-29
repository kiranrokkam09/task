from rest_framework import serializers
from .models import banks,branches

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=banks
        fields="__all__"

class BranchSerializer(serializers.ModelSerializer):
    bank_id=BankSerializer()
    class Meta:
        model=branches
        fields="__all__"