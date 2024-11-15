import tkinter as tk
from tkinter import messagebox
from src.procesamiento.regex_validator import validar_expresion
from src.graficos.automata_visualizer import AutomataVisualizer
from src.procesamiento.automata import Automata

# Función para ejecutar la validación de la expresión regular
def validar():
    cadenas_validas = []  # Para almacenar las cadenas que son válidas
    expresion = entrada_expresion.get("1.0", tk.END).strip()
    cadenas = entrada_cadenas.get("1.0", tk.END).splitlines()

    # Validar las cadenas
    resultados = validar_expresion(expresion, cadenas)

    # Mostrar los resultados en el área de resultados
    area_resultados.config(state=tk.NORMAL)
    area_resultados.delete("1.0", tk.END)
    if isinstance(resultados, str):  # En caso de error
        area_resultados.insert(tk.END, resultados)
    else:
        for cadena, es_valida in resultados:
            resultado = f"{cadena}: {'Aceptada' if es_valida else 'Rechazada'}\n"
            area_resultados.insert(tk.END, resultado)
            if es_valida:
                cadenas_validas.append(cadena)  # Solo añadir las cadenas válidas

    area_resultados.config(state=tk.DISABLED)

    # Construir y visualizar el autómata basado en la cadenas validas
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

# Entrada para las cadenas a validar
tk.Label(ventana, text="Cadenas (una por línea):").pack()
entrada_cadenas = tk.Text(ventana, height=10, width=50)
entrada_cadenas.pack()

# Botón para iniciar la validación
boton_validar = tk.Button(ventana, text="Validar", command=validar)
boton_validar.pack()

# Área de resultados
tk.Label(ventana, text="Resultados:").pack()
area_resultados = tk.Text(ventana, height=10, width=50, state=tk.DISABLED)
area_resultados.pack()

ventana.mainloop()
