'''
Created on 19 dic 2024

@author: AGUSTIN
'''
from dataclasses import dataclass
from typing import List, Dict,Set
from src.entrega3.grafo import Grafo

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones >= 0:
            return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)
        return None

    @staticmethod
    def parse(cadena: str):
        partes = cadena.strip().split(',')
        if len(partes) == 4:
            nombre = partes[0].strip()
            tipo = partes[1].strip()
            try:
                num_mutaciones = int(partes[2].strip())
                loc_cromosoma = partes[3].strip()
                return Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)
            except ValueError:
                return None
        return None



@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float):
        if -1 <= conexion <= 1:
            return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)
        return None

    @staticmethod
    def parse(cadena: str):
        partes = cadena.strip().split(',')
        if len(partes) == 3:
            nombre_gen1 = partes[0].strip()
            nombre_gen2 = partes[1].strip()
            conexion = float(partes[2].strip())
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)
        
        
    @property
    def coexpresados(self):
        return self.conexion > 0.75

    @property
    def antiexpresados(self):
        return self.conexion < -0.75



class RedGenica(Grafo[str, RelacionGenAGen]):
    def __init__(self, es_dirigido: bool = False):
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def parse(archivo_genes: str, archivo_relaciones: str, es_dirigido: bool = False):
        red = RedGenica(es_dirigido)
        
        with open(archivo_genes, 'r') as f:
            for linea in f:
                gen = Gen.parse(linea)
                if gen:
                    red.genes_por_nombre[gen.nombre] = gen
                    red.add_vertex(gen.nombre)

        
        with open(archivo_relaciones, 'r') as f:
            for linea in f:
                relacion = RelacionGenAGen.parse(linea)
                if relacion:
                    red.add_edge(relacion.nombre_gen1, relacion.nombre_gen2, relacion)
        return red
#test genagen
if __name__ == "__main__":
    print("test de gen a gen")
    print(Gen.of("GenA", "TipoX", 10, "Cromosoma1"))
    print(Gen.parse("GenB, TipoY, 15, Cromosoma2"))
    print(Gen.parse("GenC, TipoZ, -5, Cromosoma3"))

    relacion = RelacionGenAGen.parse("GenA, GenB, 0.8")
    if relacion:
        print(relacion)
        print(relacion.coexpresados, relacion.antiexpresados)

    print(RelacionGenAGen.parse("GenA, GenB, 1.5"))

#test para gen
if __name__ == "__main__":
    print("test de gen")
    gen1 = Gen.of("GenA", "TipoX", 10, "Cromosoma1")
    if gen1:
        print(gen1)
    else:
        print("Datos inválidos para Gen.of")

    
    cadena = "GenB, TipoY, 15, Cromosoma2"
    gen2 = Gen.parse(cadena)
    if gen2:
        print(gen2)
    else:
        print("Cadena inválida para Gen.parse")

    
    cadena_erronea = "GenC, TipoZ, -5, Cromosoma3"
    gen3 = Gen.parse(cadena_erronea)
    if gen3:
        print(gen3)
    else:
        print("Cadena inválida para Gen.parse")
#test para RedGen
if __name__ == "__main__":
    print("test de red generica")
    red = RedGenica.parse('genes.txt', 'red_genes.txt', es_dirigido=False)
    print(red)
    inicio = "KRAS"
    objetivo = "PIK3CA"
    visitados = set()  
    camino = []  
    # Pila para DFS
    pila = [(inicio, [inicio])]  

    while pila:
        actual, camino_actual = pila.pop()
    
        
        if actual in visitados:
            continue
    
       
        visitados.add(actual)
    
        
        if actual == objetivo:
            camino = camino_actual
            break
    
        
        for sucesor in red.successors(actual):
            if sucesor not in visitados:
                pila.append((sucesor, camino_actual + [sucesor]))
    if camino:
       print(f"Camino encontrado: {' -> '.join(camino)}")
    else:
     print("No hay camino")

        
    if camino:
        vertices_camino = set(camino)  
        subgrafo = red.subgraph(vertices_camino)  
    
    
    subgrafo.draw(
         titulo="Subgrafo KRAS -> PIK3CA",
        lambda_vertice=lambda v: v,  
        lambda_arista=lambda e: f"{e.conexion:.2f}"  
    )
     
