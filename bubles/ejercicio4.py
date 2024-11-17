def main():
    datos = []
    cantidad = int(input("Ingrese la cantidad de datos que desea ingresar: "))
    
    for i in range(cantidad):
        dato = input(f"Ingrese el dato {i + 1}: ")
        
        if dato.isdigit():
            datos.append(int(dato))
        elif dato.replace('.', '', 1).isdigit() and dato.count('.') == 1:
            datos.append(float(dato))
        else:
            datos.append(dato)
    
    print(f"Su lista es: {datos}")


main()
