import curses
import tabulate

ingresos_data = []
egresos_data = []

def calcular_total_ingresos():
    total = 0
    for ingreso in ingresos_data:
        total += ingreso[2]
    return total

def calcular_total_egresos():
    total = 0
    for egreso in egresos_data:
        total += egreso[2]
    return total

def mostrar_informacion(stdscr):
    stdscr.clear()
    stdscr.addstr("=== Información ===\n")
    
    # Mostrar los cálculos
    stdscr.addstr("=== Cálculos ===\n")
    total_ingresos = calcular_total_ingresos()
    total_egresos = calcular_total_egresos()
    diferencia = total_ingresos - total_egresos
    stdscr.addstr(f"Total de ingresos: {total_ingresos}\n")
    stdscr.addstr(f"Total de egresos: {total_egresos}\n")
    stdscr.addstr(f"Diferencia: {diferencia}\n")
    stdscr.addstr("\n")

    # Mostrar los ingresos
    stdscr.addstr("=== Ingresos ===\n")
    if ingresos_data:
        ingresos_headers = ["ID de ingreso", "Tipo", "Monto", "Fecha"]
        ingresos_table = tabulate.tabulate(ingresos_data, headers=ingresos_headers, tablefmt="grid")
        stdscr.addstr(ingresos_table)
    stdscr.addstr("\n")
    
    # Mostrar los egresos
    stdscr.addstr("=== Egresos ===\n")
    if egresos_data:
        egresos_headers = ["ID de egreso", "Tipo", "Monto", "Fecha"]
        egresos_table = tabulate.tabulate(egresos_data, headers=egresos_headers, tablefmt="grid")
        stdscr.addstr(egresos_table)
    stdscr.addstr("\n")
    stdscr.refresh()
    stdscr.getch()
def realizar_calculos(stdscr):
    stdscr.clear()
    stdscr.addstr("=== Cálculos ===\n")
    stdscr.addstr("Ingrese los datos necesarios para realizar los cálculos:\n")
    stdscr.addstr("Monto inicial: ")
    stdscr.refresh()
    monto_inicial = float(stdscr.getstr().decode())
    stdscr.addstr("Ingresos adicionales: ")
    stdscr.refresh()
    ingresos_adicionales = float(stdscr.getstr().decode())
    stdscr.addstr("Egresos adicionales: ")
    stdscr.refresh()
    egresos_adicionales = float(stdscr.getstr().decode())
    stdscr.addstr("\n")

    monto_final = monto_inicial + ingresos_adicionales - egresos_adicionales

    stdscr.addstr("=== Resultado ===\n")
    stdscr.addstr(f"Monto final: {monto_final}\n")
    stdscr.refresh()
    stdscr.getch()
def main(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Establecer colores personalizados
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Loop principal del programa
    while True:
        # Borrar la pantalla y mostrar el menú principal
        stdscr.clear()
        stdscr.addstr("=== Menú principal ===\n")
        stdscr.addstr("1. Mostrar información\n")
        stdscr.addstr("2. Realizar cálculos\n")
        stdscr.addstr("3. Salir\n")
        stdscr.addstr("Ingrese una opción: ")
        stdscr.refresh()

        # Leer la opción seleccionada por el usuario
        opcion = stdscr.getstr().decode()

        # Procesar la opción seleccionada
        if opcion == "1":
            mostrar_informacion(stdscr)
        elif opcion == "2":
            realizar_calculos(stdscr)
        elif opcion == "3":
            break  # Salir del programa