from .models import Wallet


def convertCedisToPesewas(amount):
    amount *= 100
    return amount


def convertPesewasToCedis(amount):
    amount /= 100
    return amount


def updateBalance(balance, amount):
    balance -= amount
    return balance


def findPrimaryWallet(wallet):
    qs = Wallet.objects.filter(wallet=wallet).first()
    return qs
