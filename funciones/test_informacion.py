from informacion import agregar_nombre, agregar_edad, paciente_mayor_menor, informacion

# Datos a ingresar
pacientes = [
    "Antonio Moreno 2000",
    "Carmen Díaz 2001",
    "Fernando García 2003",
    "Teresa Rodríguez 2004",
    "José López 2005",
    "Miguel Ángel Ortiz 1999",
    "Lucia Gómez 2000",
    "Francisco Javier Sánchez 2001",
    "Beatriz Domínguez 2002",
    "Adrián López 2011",
    "Martina Pascual 2012",
    "Álvaro Torres 2013",
    "Berta Romero 2014",
]

# Procesar los datos
for paciente in pacientes:
    partes = paciente.rsplit(' ', 1)  # Dividir el nombre del año de nacimiento
    nombre_completo = partes[0]
    año_nacimiento = partes[1]
    
    agregar_nombre(nombre_completo)
    agregar_edad(año_nacimiento)

print (informacion())


paciente_mayor_menor()
