def añadir_plato(menu):
    plato = input("Ingrese el nombre del plato que desea añadir: ").capitalize()
    if plato in menu:
        print(f"El plato '{plato}' ya está en el menú.")
    else:
        menu.append(plato)
        print(f"Plato '{plato}' añadido con éxito al menú.")


def buscar_plato(menu):
    plato = input("Ingrese el nombre del plato que desea buscar: ").capitalize()
    if plato in menu:
        print(f"El plato '{plato}' está en el menú.")
    else:
        print(f"El plato '{plato}' no está en el menú.")


def eliminar_plato(menu):
    plato = input("Ingrese el nombre del plato que desea eliminar: ").capitalize()
    if plato in menu:
        menu.remove(plato)
        print(f"El plato '{plato}' ha sido eliminado del menú.")
    else:
        print(f"El plato '{plato}' no está en el menú.")


def mostrar_menu(menu):
    if menu:
        print("Platos disponibles en el menú:")
        for i, plato in enumerate(menu, 1):
            print(f"{i}. {plato}")
    else:
        print("El menú está vacío.")


def main():
    menu = []
    while True:
        print("\n--- Menú del restaurante Segunda es Todo ---")
        print("1. Añadir plato al menú.")
        print("2. Buscar en el menú.")
        print("3. Eliminar plato del menú.")
        print("4. Mostrar platos del menú.")
        print("5. Salir.")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            añadir_plato(menu)
        elif opcion == 2:
            buscar_plato(menu)
        elif opcion == 3:
            eliminar_plato(menu)
        elif opcion == 4:
            mostrar_menu(menu)
        elif opcion == 5:
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")



main()
