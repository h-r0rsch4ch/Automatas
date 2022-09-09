import tkinter as tk
from tkinter import ttk
import re


# Boton Borrar
def delete():
    inputCadena.delete(0,'end')

# Validacion de la cadena
def validacionCadena():
    regex = re.compile(r"([0-4]+)(\.)?((a|c|d|e|h|i|m|n|o|q|r|u|[0-4]+)+(\.)?)*(erm)+(\.)?((a|c|d|e|h|i|m|n|o|q|r|u|[0-4]+)+(\.))*2034212")
    cadena = str(inputCadena.get())
    if re.fullmatch(regex, cadena):
        etiquetaResultado.config(text=f"La cadena {cadena} es valida.\n\n Presione borra para una nueva cadena")
    else:
        etiquetaResultado.config(text=f"La cadena {cadena} no es valida.\n\n Presione borra para una nueva cadena")

# Configuracion de la ventana
ventana = tk.Tk()
ventana.title("Actividad 1")
ventana.config(width=400, height=200)

# Etiqueta
etiquetaCadena = ttk.Label(text="Cadena a verificar:")
etiquetaCadena.place(x=20, y=20)

# Input
inputCadena = ttk.Entry()
inputCadena.place(x=22, y=40, width=360)

# Boton
botonCadena = ttk.Button(text="Comprobar", command=validacionCadena)
botonCadena.place(x=22, y=65)

# Boton Borrar
botonBorrar = ttk.Button(text="Borrar", command=delete)
botonBorrar.place(x=22, y=80)

# Resultado Validacion
etiquetaResultado = ttk.Label(text="")
etiquetaResultado.place(x=22, y=130)

ventana.mainloop()
