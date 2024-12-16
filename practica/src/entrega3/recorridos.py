'''
Created on 21 nov 2024

@author: damat

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from typing import TypeVar, List,Dict, Set

from src.entrega3.grafo import Grafo 

from src.entrega2.entrega2 import Cola 
from src.entrega2.entrega2 import Pila 

# Importa la clase Grafo desde su módulo

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas


def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
     visitados = set()  # Conjunto para marcar los vértices visitados
     cola = Cola.of()   # Cola para BFS
     cola.add(inicio)   # Agregar el vértice inicial
     predecesores = {inicio: None}  # Diccionario para almacenar los predecesores

     while len(cola._items) > 0:
        vertice = cola.remove()  # Obtener el vértice de la cola

        if vertice == destino:
            return reconstruir_camino(predecesores, destino)  # Si llegamos al destino, reconstruir el camino

        if vertice not in visitados:
            visitados.add(vertice)  # Marcar el vértice como visitado

            # Obtener los sucesores del vértice
            sucesores = grafo.successors(vertice)

            for vecino in sucesores:  # Ya no necesitamos convertirlo en lista
                if vecino not in visitados and vecino not in cola._items:
                    cola.add(vecino)  # Agregar el vecino a la cola
                    predecesores[vecino] = vertice  # Registrar el predecesor

     return []  # Si no se encuentra el destino, devolver una lista vacía

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados = set()
    pila = Pila.of()  # Pila para DFS
    pila.add(inicio)
    predecesores = {inicio: None}

    while len(pila._elements) > 0:  # Verificamos si la pila tiene elementos
        vertice = pila.remove()

        if vertice == destino:
            return reconstruir_camino(predecesores, destino)

        if vertice not in visitados:
            visitados.add(vertice)

            for vecino in reversed(list(grafo.successors(vertice))):  # Para DFS se recorre al revés
                if vecino not in visitados and vecino not in predecesores:
                    pila.add(vecino)
                    predecesores[vecino] = vertice

    return []  # Si no se encuentra el destino, devolver una lista vacía


def reconstruir_camino(predecesores: dict, destino: V) -> List[V]:
    camino = []
    vertice_actual = destino

    while vertice_actual is not None:
        camino.append(vertice_actual)  # Agregar el vértice al final de la lista
        vertice_actual = predecesores.get(vertice_actual)  # Obtener el predecesor

    return camino[::-1]  # Devolver el camino al revés