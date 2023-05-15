import db #cambia 'import database' a import DB
import ingresos
import egresos

def mostrar_datos():
    db_instance = db.Database()
    cursor = db_instance.cursor()

    # Mostrar ingresos
    cursor.execute("SELECT * FROM ingresos")
    ingresos = cursor.fetchall()
    print("\033[1;34;40m"+"Ingresos:" + "\033[0m")
    for ingreso in ingresos:
        print(f"Monto: {ingreso[1]} - Descripción: {ingreso[2]}")

    # Mostrar egresos
    cursor.execute("SELECT * FROM egresos")
    egresos = cursor.fetchall()
    print("\033[1;31;40m"+"Egresos:" + "\033[0m")
    for egreso in egresos:
        print(f"Monto: {egreso[1]} - Descripción: {egreso[2]}")

    cursor.close()
    db_instance.close()


def main():
    while True:
        print("\033[1;32;40m"+"Menú principal:" + "\033[0m")
        print("1. Agregar ingreso")
        print("2. Agregar egreso")
        print("3. Mostrar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresos.agregar_ingreso()
        elif opcion == "2":
            egresos.agregar_egreso()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            break
        else:
            print("\033[1;31;40m"+"Opción no válida, por favor intente nuevamente." + "\033[0m")

if __name__ == "__main__":
    main()
