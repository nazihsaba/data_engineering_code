import pandas as pd
from django.db import models
from django.core.management.base import BaseCommand
from etl.models import Client, Transaction
from uuid import UUID

import pandas as pd
from django.core.management.base import BaseCommand
from etl.models import Client 

class Command(BaseCommand):
    help = "Load data into the database"

    def handle(self, *args, **kwargs):
        # Load clients
        clients_file = 'data/clients.csv'
        clients_df = pd.read_csv(clients_file)
        for _, row in clients_df.iterrows():
            Client.objects.create(
                client_id=row['client_id'],
                name=row['name'],
                email=row['email'],
                date_of_birth=row['date_of_birth'],
                country=row['country'],
                account_balance=row['account_balance']
            )

        # Load transactions
        transactions_file = 'data/transactions.xlsx'
        transactions_df = pd.read_excel(transactions_file)
        for _, row in transactions_df.iterrows():
            Transaction.objects.create(
                transaction_id=row['transaction_id'],
                client_id=row['client_id'],
                transaction_type=row['transaction_type'],
                transaction_date=row['transaction_date'],
                amount=row['amount'],
                currency=row['currency']
            )
