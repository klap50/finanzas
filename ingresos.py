import colorama
from colorama import Fore, Style
import config
import db_finanzas

colorama.init(autoreset=True)

def mostrar_ingresos():
    conn = db.create_connection()  # Asegúrate de tener la función create_connection en db_finanzas.py
    cursor = conn.cursor()
    cursor.execute("SELECT id, tipo, monto, fecha FROM ingresos")
    ingresos = cursor.fetchall()
    cursor.close()
    conn.close()

    for ingreso in ingresos:
        print(f"ID: {ingreso[0]}, Tipo: {ingreso[1]}, Monto: {ingreso[2]}, Fecha: {ingreso[3]}")

def agregar_ingreso():
    tipo = input("Ingrese el tipo de ingreso: ")
    monto = float(input("Ingrese el monto del ingreso: "))
    fecha = input("Ingrese la fecha del ingreso (YYYY-MM-DD): ")
    conn = db.create_connection()  # Asegúrate de tener la función create_connection en db_finanzas.py
    cursor = conn.cursor()
    query = "INSERT INTO ingresos (tipo, monto, fecha) VALUES (%s, %s, %s)"
    cursor.execute(query, (tipo, monto, fecha))
    conn.commit()
    cursor.close()
    conn.close()
    print("Ingreso ingresado exitosamente.")

def borrar_ingreso():
    ingreso_id = int(input("Ingrese el ID del ingreso a borrar: "))
    conn = db.create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM ingresos WHERE id = %s"
    cursor.execute(query, (ingreso_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Ingreso borrado exitosamente.")

def menu_ingresos():
    while True:
        print("\nMenú de ingresos:")
        print("1. Mostrar ingresos")
        print("2. Agregar ingreso")
        print("3. Borrar ingreso")
        print("4. Salir")
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            mostrar_ingresos()
        elif opcion == 2:
            agregar_ingreso()
        elif opcion == 3:
            borrar_ingreso()
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
