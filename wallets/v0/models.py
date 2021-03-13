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
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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

    status = models.CharField(choices=STATUS, max_length=100)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE,
                                        max_length=100)

    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)

    reference_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=3)

    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
