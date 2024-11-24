from laptop_gamaing import Laptop_Gaming
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import random
class App:
    def __init__(self,root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\User\\Documents\\modulo 6\\python\\Python-POO\\clases\\img\\1.jpg","C:\\Users\\User\\Documents\\modulo 6\\python\\Python-POO\\clases\\img\\2.jpg",
               "C:\\Users\\User\\Documents\\modulo 6\\python\\Python-POO\\clases\\img\\3.jpg",
               "C:\\Users\\User\\Documents\\modulo 6\\python\\Python-POO\\clases\\img\\4.jpg",
               "C:\\Users\\User\\Documents\\modulo 6\\python\\Python-POO\\clases\\img\\5.jpg"
        ]

        root.title("Ingresar Datos")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row= 0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.root, text="Procesador").grid(row= 1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root, text="Memoria").grid(row= 2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root, text="Tarejeta Grafica").grid(row= 3,column=0)
        self.tar_grafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tar_grafica).grid(row=3,column=1)

        ttk.Label(self.root, text="Precio").grid(row= 4,column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=4,column=1)

        ttk.Button(self.root, text="Agregar Laptop", command = self.agregar_laptop).grid(row=5,column=0)

        self.mostrar_laptop = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptop.grid(row=6,column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, height=200, width=200)
        self.canva.grid(row=1 ,column=3, rowspan=6)


    def mostar_imagen_aletorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image = photo)
        self.canva.image = photo  
        pass 

    def agregar_laptop(self):
        nueva_laptop = Laptop_Gaming(
            self.marca.get(), 
            self.procesador.get(),
            self.memoria.get(),
            self.tar_grafica.get(),
            self.precio.get()
        )
        self.laptops.append(nueva_laptop)
        self.mostrar_laptop.insert(tk.END,f"{nueva_laptop}")
        self.mostar_imagen_aletorias()

        pass 



root  = tk.Tk()
app = App(root)


root.mainloop()