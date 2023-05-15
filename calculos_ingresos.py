import database

def calcular_total_ingresos():
    ingresos = database.obtener_ingresos()
    total = sum(ingreso[2] for ingreso in ingresos)
    return total

def calcular_promedio_ingresos():
    ingresos = database.obtener_ingresos()
    cantidad = len(ingresos)
    total = sum(ingreso[2] for ingreso in ingresos)
    promedio = total / cantidad if cantidad > 0 else 0
    return promedio

# Otras funciones de cálculos de ingresos

# Ejemplo de función para obtener el ingreso más alto
def obtener_ingreso_maximo():
    ingresos = database.obtener_ingresos()
    if ingresos:
        ingreso_maximo = max(ingresos, key=lambda x: x[2])
        return ingreso_maximo
    return None

# Ejemplo de función para obtener el ingreso mínimo
def obtener_ingreso_minimo():
    ingresos = database.obtener_ingresos()
    if ingresos:
        ingreso_minimo = min(ingresos, key=lambda x: x[2])
        return ingreso_minimo
    return None
