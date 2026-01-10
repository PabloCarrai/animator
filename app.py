from tkinter import *
from tkinter import messagebox as ms
from random import randint as rd


class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.etiquetaNombre = Label(self.ventana, text="Nombre")
        self.ventana.title("Animator")
        self.etiquetaNombre.grid(column=0, row=0, padx=10, pady=10)
        self.datoNombre = StringVar()
        self.entradaNombre = Entry(self.ventana, textvariable=self.datoNombre)
        self.entradaNombre.grid(column=1, row=0, padx=10, pady=10)
        self.botonAnimador = Button(
            self.ventana, text="Animame Fiera!!!", command=self.animadorCongenito
        )
        self.botonAnimador.grid(column=1, row=1, padx=10, pady=10)
        self.ventana.mainloop()

    def dialogosaLoPavo(self, n):
        for i in range(n):
            ms.showinfo(
                f"Alerta {self.entradaNombre.get()}",
                f"Hoy es tu dia {self.entradaNombre.get()} a no aflojar",
            )

    def animadorCongenito(self):
        self.dialogosaLoPavo(rd(1, 3))


prueba = Ventana()
