from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Pet
        fields = ['id', 'name', 'email', 'pet_category', 'pet_name', 'user']
