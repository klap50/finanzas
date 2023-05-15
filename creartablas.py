import database

def create_tables():
    conn = database.create_connection()
    cursor = conn.cursor()

    # Crear la tabla ingresos
    cursor.execute("""
        CREATE TABLE ingresos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            monto DECIMAL(10, 2) NOT NULL,
            descripcion VARCHAR(255) NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

# Llamada a la función para crear las tablas
create_tables()
