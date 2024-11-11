
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar,Tuple


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
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)
    
    º
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements
from typing import Callable, Generic, List, TypeVar


E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenada(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order  

    
    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'ListaOrdenada[E, R]':
        return cls(order)

   
    def __index_order(self, e: E) -> int:
        return next((i for i, current in enumerate(self._elements) if self._order(e) < self._order(current)), len(self._elements))

   
    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)

    # Representación de la lista ordenada
    def __repr__(self) -> str:
        return f'ListaOrdenada({", ".join(map(repr, self._elements))})'
    
    
from typing import Callable, Generic, List, TypeVar

E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenadaSinRepeticion(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'ListaOrdenadaSinRepeticion[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        return next((i for i, current in enumerate(self._elements) if self._order(e) < self._order(current)), len(self._elements))

    def add(self, e: E) -> None:
        if e not in self._elements:
            self._elements.insert(self.__index_order(e), e)

    def __repr__(self) -> str:
        return f'ListaOrdenadaSinRepeticion({", ".join(map(repr, self._elements))})'
    
    
    


from typing import TypeVar, Generic, List


E = TypeVar('E')

class Cola(Generic[E]):
    

    def __init__(self):
        self._items: List[E] = []  

    @staticmethod
    def of() -> 'Cola[E]':
        
        return Cola()

    def add(self, e: E) -> None:
        
        self._items.append(e)

    def remove(self) -> E:
        
        if not self._items:
            raise IndexError("La cola está vacía")
        return self._items.pop(0)

    def peek(self) -> E:
        
        if not self._items:
            raise IndexError("La cola está vacía")
        return self._items[0]
    
    
    
E = TypeVar('E')  
P = TypeVar('P')  

class ColaDePrioridad(Generic[E, P]):
    

    def __init__(self):
        self._items: List[Tuple[E, P]] = []  

    def add(self, e: E, priority: P) -> None:
        
        self._items.append((e, priority))
        self._items.sort(key=lambda x: x[1])  

    def remove(self) -> E:
        
        if not self._items:
            raise IndexError("La cola está vacía")
        return self._items.pop(0)[0]  
    def is_empty(self) -> bool:
        
        return not self._items

    def size(self) -> int:
        
        return len(self._items)




E = TypeVar('E')  

class Pila:
    

    def __init__(self):
        self._elements: List[E] = []

    @staticmethod
    def of() -> 'Pila':
        
        return Pila()

    def add(self, e: E) -> None:
        
        self._elements.append(e)

    def remove(self) -> E:
        
        if not self._elements:
            raise IndexError("La pila está vacía")
        return self._elements.pop()

    def is_empty(self) -> bool:
        
        return not self._elements
