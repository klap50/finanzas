import database

from colorama import init, Fore, Style

def mostrar_menu_egresos():
    init(autoreset=True)

    while True:
        print(Fore.GREEN + "-------- EGRESOS --------")
        print(Fore.YELLOW + "1. Mostrar registros")
        print(Fore.YELLOW + "2. Agregar registro")
        print(Fore.YELLOW + "3. Borrar registro")
        print(Fore.RED + "4. Volver atrás")
        opcion = input(Style.BRIGHT + "Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_registros("Egreso")
        elif opcion == "2":
            agregar_registro("Egreso")
        elif opcion == "3":
            borrar_registro("Egreso")
        elif opcion == "4":
            break
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente.")

def agregar_registro(tipo):
    connection = database.establecer_conexion()
    cursor = connection.cursor()

    descripcion = input("Ingrese la descripción: ")
    monto = float(input("Ingrese el monto: "))

    insert_query = "INSERT INTO finanzas (descripcion, monto, tipo) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (descripcion, monto, tipo))

    connection.commit()
    print("Registro agregado con éxito.")

    connection.close()


def borrar_registro(tipo):
    connection = database.establecer_conexion()
    cursor = connection.cursor()

    id_registro = input("Ingrese el ID del registro a borrar: ")

    delete_query = "DELETE FROM finanzas WHERE id = %s AND tipo = %s"
    cursor.execute(delete_query, (id_registro, tipo))

    if cursor.rowcount > 0:
        connection.commit()
        print("Registro borrado con éxito.")
    else:
        print("No se encontró el registro.")

    connection.close()


def mostrar_menu_egresos():
    while True:
        print("-------- EGRESOS --------")
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
            borrar_registro("Egreso")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
