import ingresos
import egresos

def calcular_total_ingresos():
    ingresos_data = ingresos.obtener_datos_ingresos()
    total = 0
    for ingreso in ingresos_data:
        total += ingreso[2]
    return total

def calcular_total_egresos():
    egresos_data = egresos.obtener_datos_egresos()
    total = 0
    for egreso in egresos_data:
        total += egreso[2]
    return total

def calcular_diferencia():
    total_ingresos = calcular_total_ingresos()
    total_egresos = calcular_total_egresos()
    diferencia = total_ingresos - total_egresos
    return diferencia

def agregar_ingreso(tipo, monto, fecha):
    ingreso_id = generar_id_ingreso()
    ingreso = [ingreso_id, tipo, monto, fecha]
    ingresos_data = ingresos.obtener_datos_ingresos()
    ingresos_data.append(ingreso)
    ingresos.actualizar_datos_ingresos(ingresos_data)

def agregar_egreso(tipo, monto, fecha):
    egreso_id = generar_id_egreso()
    egreso = [egreso_id, tipo, monto, fecha]
    egresos_data = egresos.obtener_datos_egresos()
    egresos_data.append(egreso)
    egresos.actualizar_datos_egresos(egresos_data)

def eliminar_ingreso(ingreso_id):
    ingresos_data = ingresos.obtener_datos_ingresos()
    for ingreso in ingresos_data:
        if ingreso[0] == ingreso_id:
            ingresos_data.remove(ingreso)
            break
    ingresos.actualizar_datos_ingresos(ingresos_data)

def generar_id_ingreso():
    ingresos_data = ingresos.obtener_datos_ingresos()
    if len(ingresos_data) > 0:
        last_id = ingresos_data[-1][0]
        new_id = last_id + 1
    else:
        new_id = 1
    return new_id

def generar_id_egreso():
    egresos_data = egresos.obtener_datos_egresos()
    if len(egresos_data) > 0:
        last_id = egresos_data[-1][0]
        new_id = last_id + 1
    else:
        new_id = 1
    return new_id
