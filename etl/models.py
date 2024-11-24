from django.db import models

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    account_balance = models.FloatField()

class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    transaction_date = models.DateField()
    amount = models.FloatField()
    currency = models.CharField(max_length=10)
