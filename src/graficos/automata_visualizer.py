from graphviz import Digraph

from src.procesamiento.automata import Automata


class AutomataVisualizer:
    def __init__(self, automata):
        self.automata = automata

    def visualizar(self):
        dot = Digraph()

        # Añadir nodos (estados)
        for estado in self.automata.estados:
            if estado in self.automata.estados_aceptacion:
                dot.node(estado, shape="doublecircle")
            else:
                dot.node(estado)

        # Añadir transiciones
        for (origen, simbolo), destino in self.automata.transiciones.items():
            dot.edge(origen, destino, label=simbolo)

        # Mostrar el autómata
        dot.render('automata', format='png', view=True)

# Uso de ejemplo
if __name__ == "__main__":
    automata = Automata().construir_desde_regex("^\d+$")
    visualizador = AutomataVisualizer(automata)
    visualizador.visualizar()
