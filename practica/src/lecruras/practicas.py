'''
Created on 20 oct 2024

@author: AGUSTIN
'''
def contador (fichero,sep,cad):
    with open(fichero, 'r') as fichero:
            # Leer el contenido del fichero
            contenido = fichero.read().lower()
            # Separar el contenido utilizando el separador dado
            terminos = contenido.split(sep)
            # Contar las ocurrencias de la palabra buscada
            contador = terminos.count(cad)
            return contador
    
    
    
print(contador('lin_quijote.txt','n/', 'Quijote'))


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




