from database import establecer_conexion


def mostrar_registros(tipo):
    connection = establecer_conexion()
    cursor = connection.cursor()

    print("-------------------------")
    print("ID | Descripción | Monto")
    print("-------------------------")

    select_query = "SELECT id, descripcion, monto FROM finanzas WHERE tipo = %s"
    cursor.execute(select_query, (tipo,))
    records = cursor.fetchall()

    for record in records:
        id_registro = record[0]
        descripcion = record[1]
        monto = record[2]

        print(f"{id_registro} | {descripcion} | {monto:.2f}")

    connection.close()


def agregar_registro(tipo):
    connection = establecer_conexion()
    cursor = connection.cursor()

    descripcion = input("Ingrese la descripción: ")
    monto = float(input("Ingrese el monto: "))

    insert_query = "INSERT INTO finanzas (descripcion, monto, tipo) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (descripcion, monto, tipo))

    connection.commit()
    print("Registro agregado con éxito.")

    connection.close()


def borrar_registro(tipo):
    connection = establecer_conexion()
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


def mostrar_menu_ingresos():
    while True:
        print("-------- INGRESOS --------")
        print("1. Mostrar registros")
        print("2. Agregar registro")
        print("3. Borrar registro")
        print("4. Volver atrás")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_registros("ingreso")
        elif opcion == "2":
            agregar_registro("ingreso")
        elif opcion == "3":
            borrar_registro("ingreso")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
