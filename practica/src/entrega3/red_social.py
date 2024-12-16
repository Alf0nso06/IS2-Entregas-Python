from __future__ import annotations

from dataclasses import dataclass 
from typing import Dict
from datetime import date, datetime
from src.entrega3.recorridos import bfs, dfs
from src.entrega3.grafo import Grafo

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos} ({self.dni})"

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.
    
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)
    
    def __str__(self) -> str:
        pass

class Red_social(Grafo[Usuario, Relacion]):
    """
    Representa una red social basada en el grafo genérico.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
     return Red_social(es_dirigido)

    
    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
         red = Red_social(es_dirigido)
        # Leer archivo de usuarios
         with open(f1, 'r', encoding='utf-8') as file_usuarios:
            for linea in file_usuarios:
                dni, nombre, apellidos, fecha_nacimiento = linea.strip().split(',')
                # Creamos el usuario y lo añadimos al grafo
                usuario = Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
                red.add_vertex(usuario)
                red.usuarios_dni[dni] = usuario  # Guardamos en el diccionario para facilitar las relaciones

        # Leer archivo de relaciones
         with open(f2, 'r', encoding='utf-8') as file_relaciones:
            for linea in file_relaciones:
                dni_origen, dni_destino, interacciones, dias_activa = linea.strip().split(',')
                # Creamos la relación
                relacion = Relacion.of(int(interacciones), int(dias_activa))
                # Añadimos la relación al grafo
                red.add_edge(red.usuarios_dni[dni_origen], red.usuarios_dni[dni_destino], relacion)

         return red
  

if __name__ == '__main__':
    
    rrss = Red_social.parse('usuarios (1).txt', 'relaciones (1) - copia.txt', es_dirigido=False)

    

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
        
