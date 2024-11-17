def validar_velocidad(pais, zona, velocidad):
    limites = {
        "Ecuador": {
            "urbana": (10, 50),
            "rural": (51, 70),
            "perimetral": (71, 90)
        },
        "Colombia": {
            "urbana": (10, 30),
            "rural": (31, 80),
            "perimetral": (81, 100)
        },
        "Perú": {
            "urbana": (10, 40),
            "rural": (41, 60),
            "perimetral": (61, 120)
        }
    }

    min_vel, max_vel = limites[pais][zona]
    if velocidad < min_vel:
        return f"La velocidad {velocidad} Km/h es INFERIOR al límite mínimo permitido de {min_vel} Km/h en zona {zona} de {pais}."
    elif velocidad > max_vel:
        return f"La velocidad {velocidad} Km/h es SUPERIOR al límite máximo permitido de {max_vel} Km/h en zona {zona} de {pais}."
    else:
        return f"La velocidad {velocidad} Km/h está dentro del rango permitido en zona {zona} de {pais}."


def main():
    print("¡Bienvenido a KrakeTravels!")
    print("Destinos disponibles: Ecuador, Colombia, Perú")
    pais = input("Ingrese el país al que viaja: ").capitalize()

    if pais not in ["Ecuador", "Colombia", "Perú"]:
        print("País no válido. Por favor, seleccione Ecuador, Colombia o Perú.")
        return

    print("Zonas disponibles: urbana, rural, perimetral")
    zona = input("Ingrese la zona en la que se encuentra: ").lower()

    if zona not in ["urbana", "rural", "perimetral"]:
        print("Zona no válida. Por favor, seleccione urbana, rural o perimetral.")
        return

    try:
        velocidad = int(input("Ingrese la velocidad actual del vehículo (Km/h): "))
        resultado = validar_velocidad(pais, zona, velocidad)
        print(resultado)
    except ValueError:
        print("Por favor, ingrese un valor numérico para la velocidad.")

if __name__ == "__main__":
    main()