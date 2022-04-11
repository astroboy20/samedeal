from rest_framework import serializers
from .models import MTN

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTN
        fields =(
            'data_plan', 'phone_number'
            )