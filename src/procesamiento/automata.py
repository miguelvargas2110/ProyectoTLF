class Automata:
    def __init__(self):
        self.estados = []  # Lista de estados del autómata
        self.alfabeto = []  # Alfabeto del autómata
        self.transiciones = {}  # Diccionario de transiciones
        self.estado_inicial = None
        self.estados_aceptacion = []

    def construir_desde_regex(self, regex):
        # Lógica para construir el autómata desde una expresión regular
        # Este es un ejemplo simple, deberías implementar la conversión adecuada
        self.estados = ["q0", "q1", "q2"]
        self.alfabeto = ["a", "b"]
        self.transiciones = {
            ("q0", "a"): "q1",
            ("q1", "b"): "q2",
        }
        self.estado_inicial = "q0"
        self.estados_aceptacion = ["q2"]
        return self

    def obtener_transiciones(self):
        return self.transiciones
