import db_finanzas as db
import colorama
from colorama import Fore, Style
import config
import db_finanzas

colorama.init(autoreset=True)

def agregar_egreso():
    descripcion = input("Ingrese una descripción para el egreso: ")
    monto = float(input("Ingrese el monto del egreso: "))
    db_finanzas.insertar_egreso(descripcion, monto)
    print(Fore.GREEN + "Egreso agregado exitosamente." + Style.RESET_ALL)



def mostrar_egresos():
    conn = db.create_connection()  # Asegúrate de tener la función create_connection en db_finanzas.py
    cursor = conn.cursor()
    cursor.execute("SELECT id, tipo, monto, fecha FROM egresos")
    egresos = cursor.fetchall()
    cursor.close()
    conn.close()

    for egreso in egresos:
        print(f"ID: {egreso[0]}, Tipo: {egreso[1]}, Monto: {egreso[2]}, Fecha: {egreso[3]}")

def agregar_egreso():
    tipo = input("Ingrese el tipo de egreso: ")
    monto = float(input("Ingrese el monto del egreso: "))
    fecha = input("Ingrese la fecha del egreso (YYYY-MM-DD): ")
    conn = db.create_connection()  # Asegúrate de tener la función create_connection en db_finanzas.py
    cursor = conn.cursor()
    query = "INSERT INTO egresos (tipo, monto, fecha) VALUES (%s, %s, %s)"
    cursor.execute(query, (tipo, monto, fecha))  # Completa los valores faltantes
    conn.commit()
    cursor.close()
    conn.close()
    print("Egreso agregado exitosamente.")

def borrar_egreso():
    egreso_id = int(input("Ingrese el ID del egreso a borrar: "))
    conn = db.create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM egresos WHERE id = %s"
    cursor.execute(query, (egreso_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Egreso borrado exitosamente.")

def menu_egresos():
    while True:
        print("\nMenú de egresos:")
        print("1. Mostrar egresos")
        print("2. Ingresar egreso")
        print("3. Borrar egreso")
        print("4. Salir")
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            mostrar_egresos()
        elif opcion == 2:
            ingresar_egreso()
        elif opcion == 3:
            borrar_egreso()
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
