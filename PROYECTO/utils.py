inventory = {} #Se crea un diccionario vacio

def add_product(name, price, quantity):#funcion para añadir el nombre del producto y el precio
    """Añade o actualiza un producto en el inventario."""
    if name in inventory:
        inventory[name] = (price, inventory[name][1] + quantity)
    else:
        inventory[name] = (price, quantity)
    print(f"Producto '{name}' ✅añadido/actualizado correctamente.")

def view_product(name): #Lo que hace es consultar el producto si esta  y sino no lo encontrara
    """Consulta los detalles de un producto."""
    if name in inventory:
        price, quantity = inventory[name]
        print(f"Producto: {name}, ✅Precio: 💲{price}, Cantidad: {quantity}")
    else:
        print(f"Producto '{name}' ❌no encontrado.")

def update_price(name, new_price): #Actualiza el precio del producto si el usuario selecciona la opcion
    """Actualiza el precio de un producto."""
    if name in inventory:
        quantity = inventory[name][1]
        inventory[name] = (new_price, quantity)
        print(f"Precio de '{name}' ✅actualizado a 💲{new_price}.")
    else:
        print(f"Producto '{name}' ❌no encontrado.")

def remove_product(name): #Lo que hace esta funcion dependiendo de la opcion es eliminar el producto
    """Elimina un producto del inventario."""
    if name in inventory:
        del inventory[name]
        print(f"Producto '{name}' ✅eliminado.")
    else:
        print(f"Producto '{name}' ❌no encontrado.")

def calculate_total_value(): #Calcula el valor final de todos los productos ingresados desde teclado
    """Calcula el valor total del inventario."""
    total = sum(price * quantity for price, quantity in inventory.values())
    print(f"Valor total del inventario: 💲{total}")
