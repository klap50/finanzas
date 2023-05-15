import database

def agregar_ingreso():
    while True:
        print("\033[1;34;40m"+"Agregar ingreso:" + "\033[0m")
        
        monto = float(input("Ingrese el monto del ingreso: "))
        descripcion = input("Ingrese una descripción del ingreso: ")

        conn = database.create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO ingresos (monto, descripcion) VALUES (%s, %s)"
        cursor.execute(query, (monto, descripcion))
        conn.commit()
        cursor.close()
        conn.close()

        print("\033[1;32;40m"+"Ingreso agregado correctamente." + "\033[0m")

        cancelar = input("Ingrese '4' para cancelar o cualquier otra tecla para continuar: ")
        if cancelar == "4":
            break
