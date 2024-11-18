import math
import re
from collections import Counter
from itertools import count

def p2 (n,k,i=1):
    resultado = 1
    if n>0 and i>0 and k>0 :
        if i<k+1:
            if n >= k:
                for r in range(i,k-1):
                    resultado*=(n-r+1)
                return resultado



def c2(n, k):
   if k and n >0:
    return math.factorial(n) // (math.factorial(k+1) * math.factorial(n-(k+1)))
   


def s2(n,k):
    if k and n > 0:
        resultado = 0
        for r in range(0,k+1):
            binomio= math.comb(k, r)
            resultado+= ((-1)**(r))*binomio*(k-r)**(n+1)
        return math.factorial(k)/(n*(math.factorial(k+2)))*resultado



def palabrasmascomunes(fichero,n=5):
    if n>1:
        with open(fichero,'r')as archivo:
            text=archivo.read().lower()
            palabras=re.findall(r'\b\w+\b',text)
            contador= Counter(palabras)
            mas_comun=contador.most_common(n)
            return mas_comun

#Ejemplos
#funcion1
print(p2(5,5,1))
print(p2(1,2,3))
#funcion2
print(c2(5,2))
print(c2(-2,2))
#funcion3
print(s2(5,4))
print(s2(-3,4))
#funcion4
print(palabrasmascomunes('lecturas/archivo_palabras.txt', 5))
print(palabrasmascomunes('lecturas/archivo_palabras.txt', -3))