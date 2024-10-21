'''
Created on 20 oct 2024

@author: AGUSTIN
'''

import re
separador=r'[;, \n]+'

def contador (fichero,cad):
    with open(fichero, 'r') as fichero:
            contenido = fichero.read().lower()
            terminos = re.split(separador,contenido)
            contador = terminos.count(cad.lower())
            return contador
 
 
    
print(contador('lin_quijote.txt', 'Quijote'))


def encontrar_lineas_con_cadena(nombre_fichero, cad):
    cad = cad.lower()
    lineas_encontradas = []
    with open(nombre_fichero, 'r') as f:
        
        for linea in f:
            
            if cad in linea.lower():
                lineas_encontradas.append(linea.strip())  
    
    return lineas_encontradas

print(encontrar_lineas_con_cadena('lin_quijote.txt', 'quijote'))




def palabras_unicas(nombre_fichero):
    palabras_unicas = set()
    with open(nombre_fichero, 'r') as f:
        for linea in f:
            palabras = linea.lower().split()
            palabras_unicas.update(palabras)
    
    return list(palabras_unicas)
print(palabras_unicas("lin_quijote.txt"))


def longitud_promedio_lineas(file_path: str,) -> float:
    with open(file_path, 'r') as file:
        lineas = file.readlines()
    
    longitudes = [len(line.strip().split(",")) for line in lineas]
    return sum(longitudes) / len(longitudes)
     




