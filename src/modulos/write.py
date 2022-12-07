'''
NAME
	write.py
    
VERSION
    1.0
    
AUTHOR
	Andres Rivera	
    
DESCRIPTION
    Modulo que escribe un archivo con los datos dados por los demas modulos

CATEGORY
	Gene Expression
    
USAGE
    from write import wrfile

    wrFile(protN, tema, articulos, Ids, NumArts)
'''

from crearTermino import crearTerm
import io

def wrFile(protN, tema, articulos, Ids, NumArts):

    file = io.open("Outpt.txt", "w", encoding='utf-8')
    txt = f'Proteina:\t{protN}\nTema:\t{tema}'
    txt += f'\nTermino de Busqueda:\t{crearTerm(protN, tema)}'
    txt += f'\nArticulos Encontrados:\t{NumArts}\n'
    txt += '\nPrimeros 3 Articulos Encontrados:'

    for articulo in articulos:
        txt += f'\n\nTitulo:\t{articulo["Titulo"]}'
        txt += f'\nAbstract:\t{articulo["Abstract"]}'
        txt += f'\nId:\t{articulo["Id"]}'

    txt += '\n\nIds de los Primeros 20 Articulos Encontrados:\n'
    i=0
    for id in Ids:
        if i == 10:
            txt+='\n'
        txt += f'{id}\t'
        i+=1

    file.write(txt)
    file.close()

    return()