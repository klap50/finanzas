import database

def calcular_total_ingresos():
    total = 0
    for ingreso in database.obtener_ingresos():
        total += ingreso[2]
    return total

def calcular_total_egresos():
    total = 0
    for egreso in database.obtener_egresos():
        total += egreso[2]
    return total

def guardar_egreso(monto, descripcion):
    database.insertar_egreso(monto, descripcion)

def obtener_detalles_egresos():
    return database.obtener_egresos()