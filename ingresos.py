import database

def mostrar_menu_ingresos():
    while True:
        print("-------- INGRESOS --------")
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
            borrar_registro("Ingreso")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_registros(tipo):
    connection = database.establecer_conexion()
    cursor = connection.cursor()
    
    print("-------------------------")
    print("ID | Descripción | Monto")
    print("-------------------------")
    
    select_query = "SELECT * FROM finanzas WHERE tipo = %s"
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
    
    connection.close()

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
