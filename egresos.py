import mysql.connector
from database import get_db_connection

def mostrar_egresos():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, descripcion, monto FROM egresos")
    egresos = cursor.fetchall()
    for egreso in egresos:
        print(f"ID: {egreso[0]}, Descripción: {egreso[1]}, Monto: {egreso[2]}")
    cursor.close()
    connection.close()

def ingresar_egreso(descripcion, monto):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO egresos (descripcion, monto) VALUES (%s, %s)"
    cursor.execute(query, (descripcion, monto))
    connection.commit()
    cursor.close()
    connection.close()

def borrar_egreso(id_egreso):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM egresos WHERE id = %s"
    cursor.execute(query, (id_egreso,))
    connection.commit()
    cursor.close()
    connection.close()

def menu():
    while True:
        print("Menú de egresos:")
        print("1. Mostrar egresos")
        print("2. Ingresar egreso")
        print("3. Borrar egreso por ID")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_egresos()
        elif opcion == "2":
            descripcion = input("Ingrese la descripción del egreso: ")
            monto = float(input("Ingrese el monto del egreso: "))
            ingresar_egreso(descripcion, monto)
        elif opcion == "3":
            id_egreso = int(input("Ingrese el ID del egreso a borrar: "))
            borrar_egreso(id_egreso)
        elif opcion == "4":
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
