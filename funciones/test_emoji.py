import emeoji

cantidad_frase = int(input("Cuantas frases desea ingresar:"))
for i in range(cantidad_frase):
    frase = input(f"Ingrese la frase {i+1}: ")
    emeoji.encontrarPalabra(frase)
    emeoji.agregar_frase(frase)