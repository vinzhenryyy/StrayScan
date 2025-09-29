from rest_framework import serializers
from .models import PetLog

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetLog
        fields = '__all__'