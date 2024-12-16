'''
Created on 21 nov 2024

@author: damat
'''


from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx


# Definición de tipos genéricos
V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    """
    Representaciónde un grafo utilizando un diccionario de adyacencia.
    """
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}  # Diccionario de adyacencia
    
    @staticmethod
    def of(es_dirigido: bool = True) -> Grafo[V, E]:
       return Grafo(es_dirigido)
    
    def add_vertex(self, vertice: V) -> None:  
       if vertice not in self.adyacencias:
        self.adyacencias[vertice] = {}

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        """Añade una arista al grafo, creando vértices si no existen."""
        if origen not in self.adyacencias:
            self.add_vertex(origen)
        if destino not in self.adyacencias:
            self.add_vertex(destino)

        self.adyacencias[origen][destino] = arista
        if not self.es_dirigido:
            self.adyacencias[destino][origen] = arista

    def successors(self, vertice: V) -> Set[V]:
        
     if vertice  in self.adyacencias:
        return set(self.adyacencias[vertice].keys())

    def predecessors(self, vertice: V) -> Set[V]:
        return {origen for origen, destinos in self.adyacencias.items() if vertice in destinos}

    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
         
         if origen in self.adyacencias and destino in self.adyacencias[origen]:
             return self.adyacencias[origen][destino]

    def vertices(self) -> Set[V]:
        
        return set(self.adyacencias.keys())
    
    def edge_exists(self, origen: V, destino: V) -> bool:
        return origen in self.adyacencias and destino in self.adyacencias[origen]

    def subgraph(self, vertices: Set[V]) -> Grafo[V, E]:
        subgrafo = Grafo(self.es_dirigido)
        for vertice in vertices:
            if vertice in self.adyacencias:
                subgrafo.add_vertex(vertice)
                for destino, peso in self.adyacencias[vertice].items():
                    if destino in vertices:
                        subgrafo.add_edge(vertice, destino, peso)
        return subgrafo

    def inverse_graph(self)-> Grafo[V, E]:
        
        if not self.es_dirigido:
            raise ValueError("El grafo no es dirigido, no se puede invertir")
        
        grafo_inverso = Grafo(es_dirigido=True)  # Crear un nuevo grafo dirigido vacío
        
        for vertice in self.vertices():
            grafo_inverso.add_vertex(vertice)  # Añadir los mismos vértices al grafo inverso
        
        # Añadir las aristas invertidas
        for origen in self.adyacencias:
            for destino, peso in self.adyacencias[origen].items():
                grafo_inverso.add_edge(destino, origen, peso)  # Invertir la dirección de la arista
        
        return grafo_inverso
         

    def draw(self, titulo: str = "Grafo", 
            lambda_vertice: Callable[[V], str] = str, 
            lambda_arista: Callable[[E], str] = str) -> None:
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        # Añadir nodos y aristas
        for vertice in self.vertices():
            G.add_node(vertice, label=lambda_vertice(vertice))  # Usamos lambda_vertice para personalizar el nodo
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista))  # Usamos lambda_arista para personalizar la arista
    
        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Distribución de los nodos
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, 
                labels=nx.get_node_attributes(G, 'label'))  # Usamos las etiquetas personalizadas de los vértices
    
        # Dibujar las etiquetas de las aristas (con la representación personalizada)
        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        plt.title(titulo)
        plt.show()
        
        
    def __str__(self) -> str:
       resultado = []
       for origen, destinos in self.adyacencias.items():
           for destino, peso in destinos.items():
               resultado.append(f"{origen} -> {destino} ({peso})")
               return "\n".join(resultado)
        
        

if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    
    # Dibujar el grafo
    grafo.draw(titulo="Mi Grafo Dirigido")
    
    grafo.inverse_graph().draw(titulo="Inverso del Grafo Dirigido")
