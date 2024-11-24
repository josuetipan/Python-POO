import random

class Laptop:
    def __init__(self,marca,procesador,memoria,costo = 500, impuestos = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuestos = impuestos

    def valor_final(self):
        return self.costo + self.impuestos
    
    def descuento(self, descuento):
        return (self.costo * descuento)/100
    
    def realizar_diagnostico_sistema(self):
        diagnostico = {
            "Marca": f"{self.marca}",
            "Procesador": f"{self.procesador}",
            "Memoria": "OK" if self.memoria >= 8 else "aumnetar memoria RAM",
            "Bateria": "OK" if random.choice([True,False]) else "Cambiar de bateria"
        }
        return diagnostico
    def realizar_informe_uso(self):
        resultado_informe = {
            "tipo":"Generica",
            "Uso Recomendado": "Tareas cotidianas",
            "Horas de uso": 5,
            "Diagostioo actual": self.realizar_diagnostico_sistema()
        }
        return resultado_informe
    
    @staticmethod
    def comparar_costo(laptop1,laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los laptops tienen el mismo costo."
        return "los costops son diferentes"
    
    @classmethod
    def asus_laptop(cls, costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca,procesador, memoria,costo)


class Laptop_Business(Laptop):
    def __init__(self, marca, modelo, ram, procesador, almacenamiento, duracion_bateria):
        super().__init__(marca, modelo, ram, procesador)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnostico_sistema(self):
        diagnostico = {
            "Marca": f"{self.marca}",
            "Procesador": f"{self.procesador}",
            "Memoria": "OK" if self.memoria >= 8 else "aumnetar memoria RAM",
            "Bateria": "OK" if random.chioce([True,False]) else "Cambiar de bateria"
        }
        return diagnostico

    def verificar_conectividad_red(self):
        conectividad = {
            "wifi_disponible": random.choice([True, False]),
            "acceso_servidor_empresarial": random.choice([True, False]),
            "latencia_aceptable": random.choice([True, False])
        }
        return conectividad
    
    
    
    def realizar_informe_uso(self):
        resultado_informe = {
            "tipo":"Generica",
            "Uso Recomendado": "Tareas cotidianas",
            "Horas de uso": 5,
            "Diagostioo actual": self.realizar_diagnostico_sistema()
        }
        return resultado_informe

# Ejemplo de uso
laptop_empresarial = Laptop_Business(
    marca="Dell",
    modelo="Latitude 5400",
    ram="16GB",
    procesador="Intel i7",
    almacenamiento="512GB SSD",
    duracion_bateria="10 horas"
)

# Diagnóstico del sistema
print("Diagnóstico del sistema:")

# Verificación de conectividad
print("\nVerificación de conectividad de red:")
print(laptop_empresarial.verificar_conectividad_red())