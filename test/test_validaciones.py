import unittest
from src.procesamiento.regex_validator import validar_expresion
from src.graficos.automata_visualizer import AutomataVisualizer


class TestRegexValidator(unittest.TestCase):
    def test_validacion_basica(self):
        regex = r"\d{3}"
        cadenas = ["123", "abc", "4567"]
        resultados = validar_expresion(regex, cadenas)
        self.assertEqual(resultados, [("123", True), ("abc", False), ("4567", False)])

if __name__ == "__main__":
    unittest.main()
