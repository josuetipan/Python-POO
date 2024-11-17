def encontrarPalabra(frase):
    if "feliz" in frase:
        print(f"El emoji que te representa es: \U0001F600")
    elif "triste" in frase:
        print(f"El emoji que te representa es: \U0001F62D")

lista = []
def agregar_frase(frase):
    lista.append(frase)
    print(f"Frase agregada con éxito!: {lista}")