from rest_framework import serializers
from . models import (
    User, Wallet
)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=55, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["tag", "password"]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        Wallet.objects.create(user=user)
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user
