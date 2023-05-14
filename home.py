import ingresos
import egresos

def mostrar_menu():
    while True:
        print("-------- MENU --------")
        print("1. Ingresos")
        print("2. Egresos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresos.mostrar_menu_ingresos()
        elif opcion == "2":
            egresos.mostrar_menu_egresos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

mostrar_menu()
