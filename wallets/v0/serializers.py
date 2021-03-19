from rest_framework import serializers
from .models import (
    User, Wallet, TransactionEvent, Transaction
)
from .services import convertCedisToPesewas


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=55, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["tag", "password"]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        Wallet.objects.create(user=user, is_primary=True)
        password = validated_data["password"]

        user.set_password(password)
        user.save()
        return user


class CreatePaymentReq(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ["sender", "recipient", "amount", "description"]

    def create(self, validated_data):
        recipient = validated_data["recipient"]
        amount = validated_data["amount"]

        user_id = User.objects.get(tag=recipient)
        destination_wallet = Wallet.objects.get(user=user_id)

        transaction = Transaction.objects.create(**validated_data,
                                                 wallet=destination_wallet,)

        TransactionEvent.objects.create(
            wallet=destination_wallet, amount=convertCedisToPesewas(amount),
            transaction=transaction, transaction_type="DEBIT",
        )

        return transaction
