import networkx as nx
import matplotlib.pyplot as plt
class StateMachine:
    '''
    Modela una máquina de estados, pero ahora será
    visual con un grafo la secuencia del flujo de
    trabajo
    '''
    def __init__(self, states, start_state, positions):
        self.states = states
        self.current_state = start_state
        self.history = []
        self.positions = positions  # Diccionario con las posiciones fijas de los nodos

        # Crear un grafo dirigido
        self.G = nx.DiGraph()

    def execute(self, data):
        self.history.append("Start")
        while self.current_state is not None:
            if self.current_state == "End":
                self.history.append("End")
                self.update_graph()
                break
            state_obj = self.states[self.current_state]
            self.history.append(self.current_state)
            self.update_graph()
            self.current_state, data = state_obj.execute(data)
        return self.current_state, data

    def update_graph(self):
        plt.figure(figsize=(10, 8))
        nx.draw(self.G, self.positions, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_color='purple', edge_color='gray')

        # Dibujar las etiquetas de los pesos de las aristas
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.positions, edge_labels=edge_labels)

        # Resaltar los nodos y aristas que se han ejecutado
        executed_edges = list(zip(self.history, self.history[1:]))
        nx.draw_networkx_edges(self.G, self.positions, edgelist=executed_edges, edge_color='green', width=2)
        nx.draw_networkx_nodes(self.G, self.positions, nodelist=self.history, node_color='green', node_size=3000)
        plt.title("Máquina de Estado")
        plt.show()

    def add_transition(self, from_state, to_state, condition=""):
        self.G.add_edge(from_state, to_state, weight=condition)