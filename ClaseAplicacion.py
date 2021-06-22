from tkinter import *
from tkinter import ttk, messagebox
from consume import OficialVenta

class Aplicacion():
    __ventana = None
    __pesos = None
    __dolares = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("290x115")
        self.__ventana.title("PESO A DOLAR")
        mainframe = ttk.Frame(self.__ventana, padding = "3 3 12 12")
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe["borderwidth"] = 2
        mainframe["relief"] = "sunken"
        self.__pesos = StringVar()
        self.__dolares = StringVar()
        self.__pesos.trace('w', self.calcular)
        self.pesosEntry = ttk.Entry(mainframe, width=7, textvariable=self.__pesos)
        self.pesosEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__dolares).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3,sticky=W)
        ttk.Label(mainframe, text="dolares").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.pesosEntry.focus()
        self.__ventana.mainloop()

    def calcular(self, *args):
        if self.pesosEntry.get() != "":
            try:
                pesos = float(self.pesosEntry.get())
                self.__dolares.set(pesos * OficialVenta)
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
            self.pesosEntry.focus()
        else:
            self.__dolares.set("")

