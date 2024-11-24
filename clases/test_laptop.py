from laptop import Laptop
from laptop_gamaing import Laptop_Gaming
laptop_pepito = Laptop("lenovo","i7",32)
laptop_amria = Laptop("lenovo","i7",32,600)

laptop_juanito = Laptop_Gaming("MSI","I7",4,"RTX 8GB")
print(laptop_juanito.realizar_diagnostico_sistema())


for numero in range (1,1001):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)


def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")

print("PEPITO")
imprimir_informe(laptop_pepito)

print("Juanito")
imprimir_informe(laptop_juanito)