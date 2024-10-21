'''
Created on 20 oct 2024

@author: 
'''

def contador (fichero,cad):
    with open(fichero,'r',encoding='utf-8') as f:
        contenido = f.read()
        separa=contenido.split()
        contar=separa.count(cad)
    return contar
    
print(contador('resources/lin_quijote.txt', 'quijote'))

