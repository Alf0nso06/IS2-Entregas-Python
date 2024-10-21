'''
Created on 20 oct 2024

@author: 
'''

def contador (fichero,sep,cad):
     with open(fichero, 'r') as f:
        
            contenido = f.read()
            
        
            palabras = contenido.split(sep)
            
            
            
            
           
            for palabra in palabras:
                if palabra.lower() == cad.lower():  
                    contador += 1 
                    return contador
    

print(contador('lin_quijote.txt','n/', 'quijote'))


lineas_encontradas:list=[]

def linea (fichero,cad):
 with open(fichero, 'r') as f:
            
            for linea in f.lower():
               
                if cad.lower() in linea:
                    lineas_encontradas.append(linea.strip()) 
                    return lineas_encontradas 
                    
                    
print(linea('lin_quijote.txt','quijote'))
