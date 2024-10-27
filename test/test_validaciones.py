import unittest
from src.procesamiento.regex_validator import validar_expresion
from src.graficos.automata_visualizer import AutomataVisualizer

class TestRegexValidator(unittest.TestCase):

    def test_resaltado_sintaxis(self):
        # Prueba para verificar el resaltado de sintaxis (simplificada)
        expresion = r"\d{2,3}"
        resultado = validar_expresion(expresion, "123")
        self.assertTrue(resultado)

    def test_visualizador_automata(self):
        # Prueba para verificar que se visualiza el autómata correctamente
        automata = {
            'estados': [0, 1],
            'transiciones': [(0, 'a', 1)]
        }
        visualizador = AutomataVisualizer(automata)
        self.assertIsNotNone(visualizador.visualizar())

if __name__ == '__main__':
    unittest.main()
