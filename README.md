HW02
ศุภโชค ไพดี 65114540642

git clone https://github.com/SPCH55/HW02.git

🔧 ขั้นตอนพื้นฐาน
-ติดตั้งไลบรารี
pip install clickhouse-connect ใน Django

-จากนั้นสร้างไฟล์ clickhouse_client.py ในแอป hw02
แล้วเอาโค้ดนี้ไปวาง
from clickhouse_connect import get_client
client = get_client(
    host='127.0.0.1',  # หรือ IP ของ WSL
    port=8123,
    username='default',
    password='',
    database='default'
)

def run_clickhouse_query(query):
    result = client.query(query)
    return result.result_rows

-สร้าง view (views.py) สำหรับแสดงผล
from django.shortcuts import render
from .clickhouse_client import run_clickhouse_query

def hw04_view(request):
    rows = run_clickhouse_query('SELECT date, clicked, int1, int2 FROM criteo LIMIT 20')
    return render(request, 'hw04.html', {'rows': rows})

-เพิ่ม URL ใน hw02/urls.py
from django.urls import path
from .views import hw04_view

urlpatterns = [
    path('hw04/', hw04_view, name='hw04'),
]

-สร้างไฟล์ template hw02/templates/hw04.html
<h2>ClickHouse Data</h2>
<table border="1">
  <tr>
    <th>Date</th><th>Clicked</th><th>Int1</th><th>Int2</th>
  </tr>
  {% for row in rows %}
  <tr>
    <td>{{ row.0 }}</td><td>{{ row.1 }}</td><td>{{ row.2 }}</td><td>{{ row.3 }}</td>
  </tr>
  {% endfor %}
</table>

-ตั้งค่า ClickHouse ใน WSL ให้เปิดรับการเชื่อมต่อ
เปิดไฟล์ /etc/clickhouse-server/config.xml
<listen_host>0.0.0.0</listen_host>
<http_port>8123</http_port>

-แล้วรีสตาร์ท ClickHouse:
sudo service clickhouse-server restart