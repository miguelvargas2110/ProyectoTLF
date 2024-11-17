class Automata:
    def __init__(self):
        self.estados = []  # Lista de estados del autómata
        self.alfabeto = []  # Alfabeto del autómata
        self.transiciones = {}  # Diccionario de transiciones
        self.estado_inicial = None
        self.estados_aceptacion = []

    def construir_desde_cadenas_validas(self, cadenas_validas):
        """
        Construye un NFA optimizado que acepte varias cadenas válidas.
        Si varias cadenas comparten un prefijo, utiliza un único conjunto de nodos para ese prefijo.
        """
        if not cadenas_validas:
            raise ValueError("No se proporcionaron cadenas válidas para construir el NFA.")

        # Inicializamos el autómata
        self.estados = ["q0"]  # El estado inicial q0
        self.estado_inicial = "q0"
        self.estados_aceptacion = []  # Lista de estados de aceptación
        self.transiciones = {}  # Diccionario de transiciones
        estado_count = 1  # Contador para nuevos estados

        for cadena in cadenas_validas:
            estado_actual = "q0"  # Siempre comenzamos desde el estado inicial

            for simbolo in cadena:
                # Verificar si ya existe una transición para el símbolo actual
                if (estado_actual, simbolo) not in self.transiciones:
                    # Si no existe, crear un nuevo estado
                    estado_siguiente = f"q{estado_count}"
                    self.estados.append(estado_siguiente)
                    self.transiciones[(estado_actual, simbolo)] = {estado_siguiente}
                    estado_count += 1
                else:
                    # Si ya existe una transición, seguimos al estado existente
                    estado_siguiente = list(self.transiciones[(estado_actual, simbolo)])[0]

                # Avanzar al siguiente estado
                estado_actual = estado_siguiente

            # Una vez procesada la cadena completa, marcar el último estado como de aceptación
            if estado_actual not in self.estados_aceptacion:
                self.estados_aceptacion.append(estado_actual)

        # Asegurarnos de que el alfabeto contenga todos los símbolos de las cadenas
        for cadena in cadenas_validas:
            for simbolo in cadena:
                if simbolo not in self.alfabeto:
                    self.alfabeto.append(simbolo)

        return self

    def obtener_transiciones(self):
        return self.transiciones