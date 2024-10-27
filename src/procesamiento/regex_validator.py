import re

# Función que valida una expresión regular contra una lista de cadenas
def validar_expresion(regex, cadenas):
    try:
        # Compilamos la expresión regular para asegurarnos de que sea válida
        patron = re.compile(regex)
        resultados = []

        for cadena in cadenas:
            # Verificar si la cadena cumple con la expresión regular
            if patron.fullmatch(cadena):
                resultados.append((cadena, True))  # Cadena aceptada
            else:
                resultados.append((cadena, False))  # Cadena rechazada

        return resultados

    except re.error as e:
        # Manejo de error en caso de que la expresión regular sea inválida
        return f"Error en la expresión regular: {e}"
