'''
Created on 3 oct 2024

@author: Alfonso
'''
import math



def multip (k,n):
   if n>k:
    resultado=1
    for i in list(range(0,k)):
       resultado*=(-i + n +1)
    return resultado

print(multip(2, 4))


def secuencia (r,a,k):
    resultado=1
    for i in range(1,k+1):
        resultado*=a*r**(i-1)
    return resultado
print(secuencia(5,3,2))

def combinatoria (n,k):
    return  math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print( combinatoria (4,2))


import math



def s(n, k):
    sumatoria = 0
    for i in list(range(0,k)):
        sumatoria += (-1)**i * (math.comb(k+1, i+1)) * (k - i)**n
    return (1 / math.factorial(k)) * sumatoria

print(s(4,2))


def f (x)->float:
    return 2*x**2
def df (x):
    return 4*x

def newton(a, e):
    xn = a
    for n in range(1000):
        
        if abs(f(xn)) <= e:
            return xn  
        
        if df(xn) == 0:
            
            return None
        xn = xn - f(xn) / df(xn)
    
    return None
    
print(newton( 3, 0.001))