import tkinter as tk
from tkinter import ttk
import re


# Validacion de la cadena
def validacionCadena():
    regex = re.compile(r"[1|2|4|6|7|9]+[l|u|i|s|j|a|n|r|m|o|c|t|ñ|e|d|1|2|4|6|7|9|ljrc]*[\.?][l|u|i|s|j|a|n|r|m|o|c|t|ñ|e|d|1|2|4|6|7|9|ljrc]*[\.1946217]")
    cadena = str(inputCadena.get())
    if re.fullmatch(regex, cadena):
        etiquetaResultado.config(text=f"La cadena {cadena} es valida.")
    else:
        etiquetaResultado.config(text=f"La cadena {cadena} no es valida.")

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

# Resultado Validacion
etiquetaResultado = ttk.Label(text="")
etiquetaResultado.place(x=22, y=130)

ventana.mainloop()

# (1|2|4|6|7|9)+ (.?) (ljrc|l|u|i|s|j|a|n|r|m|o|c|t|ñ|e|d|1|2|4|6|7|9)* (.?) ljrc (.?) (l|u|i|s|j|a|n|r|m|o|c|t|ñ|e|d|1|2|4|6|7|9)* . 1946217
