import tkinter as tk
from tkinter import messagebox
import re

from Main import validar


# Función para resaltar la sintaxis de la expresión regular
def resaltar_sintaxis(event):
    expresion = entrada_expresion.get()
    entrada_expresion.tag_remove("special", "1.0", tk.END)  # Limpiar resaltado anterior

    # Patrones a resaltar
    patrones = {
        "special": r"[\.\*\+\?\|\[\]\(\)\^\$]",  # Caracteres especiales
        "group": r"\(.*?\)",                    # Grupos ()
        "quantifier": r"\{.*?\}",               # Cuantificadores {}
        "range": r"\[.*?\]"                    # Rango []
    }

    for tag, pattern in patrones.items():
        for match in re.finditer(pattern, expresion):
            start = "1.0 + %dc" % match.start()
            end = "1.0 + %dc" % match.end()
            entrada_expresion.tag_add(tag, start, end)
            entrada_expresion.tag_config(tag, foreground="blue" if tag == "special" else "green")

# Interfaz de usuario
ventana = tk.Tk()
ventana.title("Validador de Expresiones Regulares")

# Entrada de expresión regular con resaltado
tk.Label(ventana, text="Expresión Regular:").pack()
entrada_expresion = tk.Text(ventana, height=2, width=50)
entrada_expresion.pack()
entrada_expresion.bind("<KeyRelease>", resaltar_sintaxis)

# Entrada para las cadenas a validar
tk.Label(ventana, text="Cadenas (una por línea):").pack()
entrada_cadenas = tk.Text(ventana, height=10, width=50)
entrada_cadenas.pack()

# Botón de validación
boton_validar = tk.Button(ventana, text="Validar", command=validar)
boton_validar.pack()

# Área de resultados
tk.Label(ventana, text="Resultados:").pack()
area_resultados = tk.Text(ventana, height=10, width=50, state=tk.DISABLED)
area_resultados.pack()

ventana.mainloop()
