from datetime import datetime

class Auto :
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Kilometraje: {self.kilometraje} km")
    
    def actualizar_kilometraje(self, actualizar):
        if self.kilometraje > actualizar:
            print("No se puede actualizar el kilometraje por que es menor a la actual")
        else:
            self.kilometraje += actualizar
            print(f"Kilometraje actualizado. Nuevo kilometraje: {self.kilometraje} km.")
    
    def realizar_viaje(self, viaje):
        if viaje > 0:
            self.kilometraje += viaje
            print(f"Viaje realizado. Kilometraje actual: {self.kilometraje} km.")
        else:
            print("El valor del viaje debe ser positivo.")
    
    def estado_auto(self):
        if self.kilometraje < 20000:
           print("Estoy como nuevo")
        elif self.kilometraje >= 20000 and self.kilometraje < 100000:
            print("Ya estoy usado")
        elif self.kilometraje > 100000:
            print("¡Ya déjame descansar por favor!")
    
    @classmethod
    def auto_nuevo(cls, modelo):
        anio_actual = datetime.now().year
        return cls("Toyota", modelo, anio_actual)
    
    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje
    
    @classmethod
    def auto_generico(cls):
        return cls("Genérico", "Modelo Base", 2000)
    
    @staticmethod
    def promedio_kilometraje(auto1, auto2):
        return (auto1.kilometraje + auto2.kilometraje) / 2


auto1 = Auto.auto_nuevo("Corolla")
auto2 = Auto("Honda", "Civic", 2018, 50000)
auto3 = Auto.auto_generico()

# Mostrar información de los autos
print("Información de los autos creados:")
auto1.mostrar_informacion()
auto2.mostrar_informacion()
auto3.mostrar_informacion()

# Comparar kilometraje
print("\n¿Auto1 y Auto2 tienen el mismo kilometraje?")
print("Sí" if Auto.comparar_kilometraje(auto1, auto2) else "No")

# Calcular promedio de kilometraje
promedio = Auto.promedio_kilometraje(auto1, auto2)
print(f"\nPromedio de kilometraje entre Auto1 y Auto2: {promedio:.2f} km")




# Crear un objeto Auto
mi_auto = Auto("Toyota", "Corolla", 2015)

# Mostrar información inicial
print("Información del auto:")
mi_auto.mostrar_informacion()

# Actualizar el kilometraje
print("\nIntentando actualizar el kilometraje a 10000 km:")
mi_auto.actualizar_kilometraje(10000)

# Realizar un viaje
print("\nRealizando un viaje de 500 km:")
mi_auto.realizar_viaje(500)

# Mostrar estado del auto
print("\nEstado del auto:")
mi_auto.estado_auto()

# Intentar reducir el kilometraje
print("\nIntentando actualizar el kilometraje a 8000 km:")
mi_auto.actualizar_kilometraje(8000)

# Realizar otro viaje largo
print("\nRealizando un viaje de 30000 km:")
mi_auto.realizar_viaje(30000)

# Ver el estado del auto nuevamente
print("\nEstado del auto:")
mi_auto.estado_auto()

 