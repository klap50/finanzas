import database

def agregar_egreso():
    while True:
        print("\033[1;34;40m"+"Agregar egreso:" + "\033[0m")
        
        monto = float(input("Ingrese el monto del egreso: "))
        descripcion = input("Ingrese una descripción del egreso: ")

        conn = database.create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO egresos (monto, descripcion) VALUES (%s,```
