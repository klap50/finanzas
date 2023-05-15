from db_finanzas import create_connection
import egresos
import ingresos
import calculos
from colorama import init, Fore, Style

init()  # Inicializar colorama

def mostrar_datos():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Mostrar ingresos
        cursor.execute("SELECT * FROM ingresos")
        resultados_ingresos = cursor.fetchall()
        print(Fore.GREEN + "Ingresos:" + Style.RESET_ALL)
        if len(resultados_ingresos) == 0:
            print("No se encontraron registros de ingresos.")
        else:
            total_ingresos = 0
            for ingreso in resultados_ingresos:
                total_ingresos += ingreso[1]
                print(f"ID: {Fore.GREEN}{ingreso[0]}{Style.RESET_ALL} - Monto: {Fore.YELLOW}{ingreso[1]}{Style.RESET_ALL} - Descripción: {Style.BRIGHT}{ingreso[2]}{Style.RESET_ALL}")

            print(f"Total de ingresos: {Fore.RED}{total_ingresos}{Style.RESET_ALL}")

        # Mostrar egresos
        cursor.execute("SELECT * FROM egresos")
        resultados_egresos = cursor.fetchall()
        print(Fore.RED + "Egresos:" + Style.RESET_ALL)
        if len(resultados_egresos) == 0:
            print("No se encontraron registros de egresos.")
        else:
            total_egresos = 0
            for egreso in resultados_egresos:
                total_egresos += egreso[1]
                print(f"ID: {Fore.GREEN}{egreso[0]}{Style.RESET_ALL} - Monto: {Fore.YELLOW}{egreso[1]}{Style.RESET_ALL} - Descripción: {Style.BRIGHT}{egreso[2]}{Style.RESET_ALL}")

            print(f"Total de egresos: {Fore.RED}{total_egresos}{Style.RESET_ALL}")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\033[1;32;40m"+"Menú principal:" + "\033[0m")
        print("1. Agregar ingreso")
        print("2. Agregar egreso")
        print("3. Mostrar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresos.agregar_ingreso()
        elif opcion == "2":
            egresos.ingresar_egreso()
        elif opcion == "3":
            mostrar_datos()
            calculos.mostrar_calculos()
        elif opcion == "4":
            break
        else:
            print("\033[1;31;40m"+"Opción no válida, por favor intente nuevamente." + "\033[0m")

if __name__ == "__main__":
    main()