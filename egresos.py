import db  # Cambia 'import database' a 'import db'

def mostrar_egresos():
    db_instance = db.Database()
    egresos = db_instance.query("SELECT id, descripcion, monto FROM egresos")
    db_instance.close()
    for egreso in egresos:
        print(f"ID: {egreso[0]}, Descripción: {egreso[1]}, Monto: {egreso[2]}")

def ingresar_egreso():
    descripcion = input("Ingrese la descripción del egreso: ")
    monto = float(input("Ingrese el monto del egreso: "))
    db_instance = db.Database()
    db_instance.execute("INSERT INTO egresos (descripcion, monto) VALUES (%s, %s)", (descripcion, monto))
    db_instance.close()
    print("Egreso ingresado exitosamente.")

def borrar_egreso():
    egreso_id = int(input("Ingrese el ID del egreso a borrar: "))
    db_instance = db.Database()
    db_instance.execute("DELETE FROM egresos WHERE id = %s", (egreso_id,))
    db_instance.close()
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

