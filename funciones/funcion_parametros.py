def datos (nombre, apellido,edad,emnsaje="hola"):
    if edad < 18:
        print(f"{emnsaje} {nombre} {apellido} es menor de edad ")
    else:
        print(f"{emnsaje} {nombre} {apellido} es mayor de edad ")