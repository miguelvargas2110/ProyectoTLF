class Automata:
    def __init__(self):
        self.estados = []  # Lista de estados del autómata
        self.alfabeto = []  # Alfabeto del autómata
        self.transiciones = {}  # Diccionario de transiciones
        self.estado_inicial = None
        self.estados_aceptacion = []

    def construir_desde_cadenas_validas(self, cadenas_validas):
        """
        Construye un NFA que acepte varias cadenas válidas.
        """
        if not cadenas_validas:
            raise ValueError("No se proporcionaron cadenas válidas para construir el NFA.")

        # Inicializamos el autómata
        self.estados = ["q0"]  # El estado inicial q0
        self.estado_inicial = "q0"
        estado_count = 1  # Contador para nuevos estados
        self.estados_aceptacion = []  # Lista de estados de aceptación
        self.transiciones = {}  # Diccionario de transiciones

        # Recorremos las cadenas válidas para construir las transiciones
        for cadena in cadenas_validas:
            estado_actual = "q0"  # Empezamos siempre desde el estado inicial

            # Recorremos los símbolos de la cadena
            for simbolo in cadena:
                # Si no hay una transición para este estado y símbolo, la creamos
                if (estado_actual, simbolo) not in self.transiciones:
                    self.transiciones[(estado_actual, simbolo)] = set()

                # Definimos el siguiente estado
                estado_siguiente = f"q{estado_count}"
                self.estados.append(estado_siguiente)
                self.transiciones[(estado_actual, simbolo)].add(estado_siguiente)

                # Avanzamos al siguiente estado
                estado_actual = estado_siguiente
                estado_count += 1

            # El último estado de la cadena debe ser un estado de aceptación
            self.estados_aceptacion.append(estado_actual)

        # Asegurarnos de que el alfabeto contenga todos los símbolos de las cadenas
        for cadena in cadenas_validas:
            for simbolo in cadena:
                if simbolo not in self.alfabeto:
                    self.alfabeto.append(simbolo)

        return self

    def obtener_transiciones(self):
        return self.transiciones