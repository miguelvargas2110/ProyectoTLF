from graphviz import Digraph

class AutomataVisualizer:
    def __init__(self, automata):
        self.automata = automata

    def visualizar(self):
        dot = Digraph()

        # Añadir nodos (estados)
        for estado in self.automata.estados:
            # Si el estado está en los estados de aceptación, lo marcamos como un doble círculo
            if estado in self.automata.estados_aceptacion:
                dot.node(estado, shape="doublecircle")
            else:
                dot.node(estado)

        # Añadir transiciones
        for (origen, simbolo), destinos in self.automata.transiciones.items():
            # La transición puede ser múltiple (conjunto de destinos), por eso iteramos
            for destino in destinos:
                dot.edge(origen, destino, label=simbolo)

        # Mostrar el autómata
        dot.render('automata', format='png', view=True)
