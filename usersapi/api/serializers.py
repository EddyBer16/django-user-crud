from rest_framework import serializers
from .models import UserDjango


class UserDjangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDjango
        fields = ['id', 'username', 'password']
