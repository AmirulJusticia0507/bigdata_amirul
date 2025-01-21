from rest_framework import serializers
from .models import PemainBola

class PemainBolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PemainBola
        fields = '__all__'
