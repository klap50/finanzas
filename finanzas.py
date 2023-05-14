import mysql.connector

# Establecer la conexión
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='glider911',
    database='finanzas'
)

# Obtener un objeto cursor
cursor = connection.cursor()

# Definir la sentencia SQL para crear la tabla
create_table_query = '''
CREATE TABLE IF NOT EXISTS finanzas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    monto DECIMAL(10, 2),
    tipo VARCHAR(10)
)
'''

# Ejecutar la sentencia SQL
cursor.execute(create_table_query)

# Confirmar los cambios
connection.commit()

def mostrar_registros(tipo):
    cursor.execute(f"SELECT * FROM finanzas WHERE tipo = '{tipo}'")
    records = cursor.fetchall()

    total_gastos = 0

    print("ID | Descripción | Monto")
    print("-------------------------")

    for record in records:
        registro = f"{record[0]} | {record[1]} | {record[2]}"
        print(registro)

        total_gastos += float(record[2])

    print("-------------------------")
    print(f"Total de {tipo}: {total_gastos}")


def agregar_registro(tipo):
    descripcion = input('Ingrese la descripción: ')
    monto = float(input('Ingrese el monto: '))
    insert_query = '''
    INSERT INTO finanzas (descripcion, monto, tipo)
    VALUES (%s, %s, %s)
    '''
    cursor.execute(insert_query, (descripcion, monto, tipo))
    connection.commit()
    print('Datos agregados correctamente.')


def borrar_registro():
    id_registro = int(input('Ingrese el ID del registro a borrar: '))
    delete_query = 'DELETE FROM finanzas WHERE id = %s'
    cursor.execute(delete_query, (id_registro,))
    connection.commit()
    print('Registro borrado correctamente.')


def mostrar_menu():
    while True:
        print("-------- MENU --------")
        print("1. Inicio")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_menu_inicio()
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def mostrar_menu_inicio():
    while True:
        print("-------- INICIO --------")
        print("1. Ingreso")
        print("2. Egreso")
        print("3. Volver atrás")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_menu_ingreso()
        elif opcion == "2":
            mostrar_menu_egreso()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def mostrar_menu_ingreso():
    while True:
        print("-------- INGRESO --------")
        print("1. Mostrar registros")
        print("2. Agregar registro")
        print("3. Borrar registro")
        print("4. Volver atrás")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_registros("Ingreso")
        elif opcion == "2":
            agregar_registro("Ingreso")
        elif opcion == "3":
            borrar_registro()
        elif opcion == "4":
            break
        e
