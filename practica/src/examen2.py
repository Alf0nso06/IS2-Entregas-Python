
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar,Tuple,Callable


E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
       
        self._elements: List[E] = []
    
    
    @property
    def size(self) -> int:
        return len(self._elements)
    
   
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    
    @property
    def elements(self) -> List[E]:
        return self._elements[:]
    
    
    @abstractmethod
    def add(self, e: E) -> None:
        pass
    
    
    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)
    
    
    def remove(self) -> E:
        assert len(self._elements) > 0
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements
    def contains(self,e:E):
        
        return e in self._elements
    
    def find(self,func: Callable[[E], bool]) -> E | None:
        for element in self._elements:
            if func(element):
                return element
        return None
    def filter(self, func: Callable[[E], bool]) -> list[E]:
        con:list = []
        for element in self._elements:
            if func(element):
                con.append(element)
            return con
            
            











class ColaConLimite(AgregadoLineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        assert capacidad > 0
        self.capacidad = capacidad
    
    
    @classmethod
    def of(cls, capacidad: int) -> 'ColaConLimite[E]':
        
        return cls(capacidad)
    
    @property
    def is_full(self) -> bool:
        
        return len(self._elements) >= self.capacidad
    
    @classmethod
    def add(self, e: E) -> None:
        if self.is_full:
            return "La lista esta llena"
        else:
            return self.add(e)
    
    
    
#soluciones ej 1


#soluciones ej 2  
 

 
  
    
