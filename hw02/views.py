from django.shortcuts import render
from hw02.clickhouse_client import run_clickhouse_query

def home(request):
    return render(request, 'home.html')


def hw04_view(request):
    query = "SELECT date, clicked, int1, int2 FROM criteo LIMIT 20"
    rows = run_clickhouse_query(query)
    return render(request, 'hw04.html', {'rows': rows})