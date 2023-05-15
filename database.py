import mysql.connector
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

def create_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create ingresos table
    cursor.execute("CREATE TABLE IF NOT EXISTS ingresos (id INT AUTO_INCREMENT PRIMARY KEY, monto FLOAT, descripcion VARCHAR(255))")

    # Create egresos table
    cursor.execute("CREATE TABLE IF NOT EXISTS egresos (id INT AUTO_INCREMENT PRIMARY KEY, monto FLOAT, descripcion VARCHAR(255))")

    conn.commit()
    cursor.close()
    conn.close()
