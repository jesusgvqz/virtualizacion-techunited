import pyodbc
import os

server = 'db-app-dev-server.database.windows.net'
database = 'db_app_dev'
username = 'virt'
password = 'Servicios.123' 
driver = '{ODBC Driver 17 for SQL Server}'

print("▶ Intentando conexión a la base de datos...")

try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    )
    print("✅ Conexión exitosa a la base de datos")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
