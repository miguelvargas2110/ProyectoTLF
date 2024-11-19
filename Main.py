import tkinter as tk
from tkinter import messagebox
import re

from src.graficos.automata_visualizer import AutomataVisualizer
from src.procesamiento.automata import Automata


# Función modular para resaltar la sintaxis de expresiones regulares
def resaltar_sintaxis(event):
    """
    Resalta los elementos de la expresión regular en el campo de entrada.
    """
    expresion = entrada_expresion.get("1.0", tk.END).strip()
    entrada_expresion.tag_remove("special", "1.0", tk.END)  # Limpiar resaltado anterior

    patrones = {
        "special": r"[\.\*\+\?\|\[\]\(\)\^\$]",  # Caracteres especiales
        "group": r"\(.*?\)",                    # Grupos ()
        "quantifier": r"\{.*?\}",               # Cuantificadores {}
        "range": r"\[.*?\]"                    # Rango []
    }

    colores = {
        "special": "blue",
        "group": "green",
        "quantifier": "orange",
        "range": "purple"
    }

    for tag, pattern in patrones.items():
        entrada_expresion.tag_config(tag, foreground=colores[tag])  # Configurar colores
        for match in re.finditer(pattern, expresion):
            start = f"1.0 + {match.start()}c"
            end = f"1.0 + {match.end()}c"
            entrada_expresion.tag_add(tag, start, end)

def validar_expresion(regex, cadenas):
    """
    Valida las cadenas proporcionadas contra la expresión regular.
    """
    try:
        patron = re.compile(regex)
        resultados = []
        for cadena in cadenas:
            if patron.fullmatch(cadena):
                resultados.append((cadena, True))
            else:
                resultados.append((cadena, False))
        return resultados
    except re.error as e:
        return f"Error en la expresión regular: {e}"

def validar():
    """
    Valida las cadenas proporcionadas en la interfaz contra la expresión regular.
    """
    cadenas_validas = []
    expresion = entrada_expresion.get("1.0", tk.END).strip()
    cadenas = entrada_cadenas.get("1.0", tk.END).splitlines()

    resultados = validar_expresion(expresion, cadenas)

    area_resultados.config(state=tk.NORMAL)
    area_resultados.delete("1.0", tk.END)
    if isinstance(resultados, str):  # Si hay error en la expresión
        area_resultados.insert(tk.END, resultados)
        entrada_expresion.config(bg="lightcoral")  # Indicador visual de error
    else:
        entrada_expresion.config(bg="white")  # Fondo blanco si es válido
        for cadena, es_valida in resultados:
            resultado = f"{cadena}: {'Aceptada' if es_valida else 'Rechazada'}\n"
            area_resultados.insert(tk.END, resultado)
            if es_valida:
                cadenas_validas.append(cadena)
    area_resultados.config(state=tk.DISABLED)

    if cadenas_validas.__len__() > 0:
        automata = Automata().construir_desde_cadenas_validas(cadenas_validas)
        visualizador = AutomataVisualizer(automata)
        visualizador.visualizar()

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Validador de Expresiones Regulares")

# Entrada de expresión regular
tk.Label(ventana, text="Expresión Regular:").pack()
entrada_expresion = tk.Text(ventana, height=2, width=50)
entrada_expresion.pack()
entrada_expresion.bind("<KeyRelease>", resaltar_sintaxis)

# Entrada para las cadenas a validar
tk.Label(ventana, text="Cadenas (una por línea):").pack()
entrada_cadenas = tk.Text(ventana, height=10, width=50)
entrada_cadenas.pack()

# Botón para validar
boton_validar = tk.Button(ventana, text="Validar", command=validar)
boton_validar.pack()

# Área de resultados
tk.Label(ventana, text="Resultados:").pack()
area_resultados = tk.Text(ventana, height=10, width=50, state=tk.DISABLED)
area_resultados.pack()

ventana.mainloop()
