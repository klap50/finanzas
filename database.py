import mysql.connector

def establecer_conexion():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='glider911',
        database='finanzas'
    )
    return connection

def crear_tabla(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'finanzas'")
    table_exists = cursor.fetchone()

    if not table_exists:
        create_table_query = '''
        CREATE TABLE finanzas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255),
            monto DECIMAL(10, 2),
            tipo VARCHAR(10)
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()
