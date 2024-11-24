from django.http import JsonResponse
from django.shortcuts import render
from etl.models import Transaction
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


@login_required
def client_summary(request):
    query = """
    SELECT c.name AS client_name, cs.total_transactions, cs.total_spent, cs.total_gained
    FROM client_summary cs
    INNER JOIN etl_client c ON cs.client_id = c.client_id;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return render(request, 'client_summary.html', {'clients': results})


def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
# def get_transactions(request, client_id):
#     transactions = Transaction.objects.filter(client_id=client_id)
#     return JsonResponse(list(transactions.values()), safe=False)