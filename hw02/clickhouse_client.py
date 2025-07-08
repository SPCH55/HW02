from clickhouse_connect import get_client

client = get_client(
    host='172.25.243.106',
    port=8123,
    username='default',
    password='',
    database='default'
)

def run_clickhouse_query(query):
    result = client.query(query)
    return result.result_rows