import os #Se importa la biblioteca os para poder usar el comando clear en linux
from src.utils import *

def show_menu(): #Funcion para mostrar el menu al ejecutra el programa
    """Muestra el menú principal al usuario."""
    print("\n" + "*" * 10)
    print("** GESTIÓN DE INVENTARIOS DIGITAL **")
    print("*" * 10)
    print("🧺 1. Añadir producto")
    print("🔎 2. Consultar producto")
    print("💰 3. Actualizar precio")
    print("❌ 4. Eliminar producto")
    print("💸 5. Calcular valor total")
    print("6. Salir")

def execute_option(option): #Funcion para validar si la opcion que el usuario selecciono es correcta
    """Ejecuta la opción seleccionada."""#Estas opciones estan para validar cada opcion que tiene el menu
    if option == 1:
        name = input("🏷️ Nombre del producto: ").capitalize()
        price = float(input("💲 Precio del producto: "))
        quantity = int(input("Cantidad del producto: "))
        add_product(name, price, quantity)
    elif option == 2:
        name = input("🏷️ Nombre del producto a consultar: ").capitalize()
        view_product(name)
    elif option == 3:
        name = input("🏷️ Nombre del producto a actualizar: ").capitalize()
        new_price = float(input("💲 Nuevo precio: "))
        update_price(name, new_price)
    elif option == 4:
        name = input("🏷️ Nombre del producto a eliminar: ").capitalize()
        remove_product(name)
    elif option == 5:
        calculate_total_value()
    elif option == 6:
        print("Saliendo del programa.")
        return False
    else:
        print("Opción no válida.") #Si el usuario introduce un valor que no esta en el rango ingresado dara error
    return True

def main(): #Funcion principal apenas el programa se ejecute
    """Función principal para ejecutar el programa."""
    os.system("clear") 
    running = True
    while running:
        show_menu() 
        try:
            choice = int(input("Selecciona una opción: "))
            running = execute_option(choice)
        except ValueError:
            print("Por favor, ingresa un número válido.")

main()#Se llama al menu principal
