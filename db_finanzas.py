import mysql.connector
from configparser import ConfigParser
from datetime import datetime

def get_config():
    config = ConfigParser()
    config.read('config.ini')
    return config

def create_connection():
    config = get_config()
    conn = mysql.connector.connect(
        host=config.get('database', 'DB_HOST'),
        port=config.getint('database', 'DB_PORT'),
        user=config.get('database', 'DB_USER'),
        password=config.get('database', 'DB_PASS'),
        database=config.get('database', 'DB_NAME')
    )
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create ingresos table
    cursor.execute("CREATE TABLE IF NOT EXISTS ingresos (id INT AUTO_INCREMENT PRIMARY KEY, monto FLOAT, descripcion VARCHAR(255), fecha DATE)")

    # Create egresos table
    cursor.execute("CREATE TABLE IF NOT EXISTS egresos (id INT AUTO_INCREMENT PRIMARY KEY, monto FLOAT, descripcion VARCHAR(255), fecha DATE)")

    # Create clientes table
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), email VARCHAR(255))")

    conn.commit()
    cursor.close()
    conn.close()

def insertar_ingreso(monto, descripcion):
    conn = create_connection()
    cursor = conn.cursor()
    fecha_actual = datetime.now().date()
    query = "INSERT INTO ingresos (monto, descripcion, fecha) VALUES (%s, %s, %s)"
    values = (monto, descripcion, fecha_actual)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def insertar_egreso(monto, descripcion):
    conn = create_connection()
    cursor = conn.cursor()
    fecha_actual = datetime.now().date()
    query = "INSERT INTO egresos (monto, descripcion, fecha) VALUES (%s, %s, %s)"
    values = (monto, descripcion, fecha_actual)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

create_tables()
