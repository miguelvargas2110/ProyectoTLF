import unittest
import re

# Función de validación (simplificada para pruebas)
def validar_expresion(expresion, cadena):
    try:
        return bool(re.fullmatch(expresion, cadena))
    except re.error:
        return False

# Clase de pruebas
class TestValidadorExpresionesRegulares(unittest.TestCase):

    def test_cadena_valida(self):
        self.assertTrue(validar_expresion(r'\d+', '12345'))  # Solo dígitos

    def test_cadena_invalida(self):
        self.assertFalse(validar_expresion(r'\d+', 'abc'))  # Solo letras no pasa la expresión \d+

    def test_expresion_mal_formada(self):
        self.assertFalse(validar_expresion(r'[abc', 'abc'))  # Expresión regular mal formada

if __name__ == '__main__':
    unittest.main()
