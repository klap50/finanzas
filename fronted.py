import mysql.connector
import database

connection = database.establecer_conexion()
database.crear_tabla(connection)

# Resto del código de la interfaz de usuario aquí

def mostrar_registros(tipo):
    print("-------------------------")
    print("ID | Descripción | Monto")
    print("-------------------------")
    select_query = "SELECT * FROM registros WHERE tipo = %s"
    cursor.execute(select_query, (tipo,))
    records = cursor.fetchall()
    total_gastos = 0
    for record in records:
        try:
            monto = float(record[2])
            total_gastos += monto
            print(f"{record[0]} | {record[1]} | {monto:.2f}")
        except ValueError:
            continue  # Omitir registros no válidos
    print("-------------------------")
    print(f"Total: {total_gastos:.2f}")


def agregar_registro(tipo):
    connection = establecer_conexion()
    cursor = connection.cursor()
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
    connection = establecer_conexion()
    cursor = connection.cursor()
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

#CorteChorizo

def mostrar_menu_ingreso():
    while True:
        print("-------- INGRESO --------")
        print("1. Mostrar registros")
        print("2. Agregar registro")
        print("3. Borrar registro")
        print("4. Volver atrás")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_registros("Ingreso")  # Corregir el argumento "Ingreso"
        elif opcion == "2":
            agregar_registro("Ingreso")  # Corregir el argumento "Ingreso"
        elif opcion == "3":
            borrar_registro("Ingreso")  # Corregir el argumento "Ingreso"
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def mostrar_menu_egreso():
    while True:
        print("-------- EGRESO --------")
        print("1. Mostrar registros")
        print("2. Agregar registro")
        print("3. Borrar registro")
        print("4. Volver atrás")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_registros("Egreso")
        elif opcion == "2":
            agregar_registro("Egreso")
        elif opcion == "3":
            borrar_registro()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

mostrar_menu()

