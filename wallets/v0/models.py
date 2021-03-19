from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if username is None:
            raise TypeError("Must provide username.")

        if email is None:
            raise TypeError("Must provide email.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):

        if password is None:
            raise TypeError("Password cannot be empty.")
        if email is None:
            raise TypeError("Must provide email")

        # extra_fields["phone_number"] = input("Phone Number: ")
        user = self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    tag = models.CharField(max_length=100, unique=True, db_index=True,
                           null=True)

    USERNAME_FIELD = 'tag'

    objects = UserManager()

    def __str__(self):
        return f"${self.tag}"


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


class Transaction(models.Model):
    STATUS = [
        ("PENDING", "pending"),
        ("FAILED", "failed"),
        ("SUCCESS", "success"),
    ]

    TRANSACTION_TYPE = [
        ("TRANSFER", "transfer"),
        ("DEPOSIT", "desposit"),
        ("WITHDRAWAL", "withdrawal"),
    ]

    DIRECTION = [
        ("INCOMING", "incoming"),
        ("OUTGOING", "outgoing"),
    ]

    status = models.CharField(choices=STATUS, max_length=100)
    direction = models.CharField(choices=DIRECTION, max_length=100, null=True)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE,
                                        max_length=100)

    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)

    reference_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField(null=True)

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.sender} sent {self.recipient} {self.amount}"


class TransactionEvent(models.Model):
    TYPE = [
        ("DEBIT", "debit"),
        ("CREDIT", "credit"),
    ]

    transaction_type = models.CharField(choices=TYPE, max_length=20)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
