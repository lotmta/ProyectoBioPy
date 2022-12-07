'''
NAME
	write.py
    
VERSION
    1.2
    
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

def wrFile(protN, tema, articulos, Ids, NumArts, i):

    # En caso de que tengamos mas de una secuencia en el archivo fasta, cambiamos los nombres de output
    if i == 0:
        file = io.open("Outpt.txt", "w", encoding='utf-8')
    else:
        file = io.open(f"Outpt_{i+1}.txt", "w", encoding='utf-8')

    # Se escribe en el archivo el nombre de la proteina, tema, termino de busqueda, articulos encontrados 
    # y los primeros 3 articulos encontrados
    txt = f'Proteina:\t{protN}\nTema:\t{tema}'
    txt += f'\nTermino de Busqueda:\t{crearTerm(protN, tema)}'
    txt += f'\nArticulos Encontrados:\t{NumArts}\n'
    txt += '\nPrimeros 3 Articulos Encontrados:'


    # Escribimos el titulo, abstract e Id de los 3 articulos
    for articulo in articulos:
        txt += f'\n\nTitulo:\t{articulo["Titulo"]}'
        txt += f'\nAbstract:\t{articulo["Abstract"]}'
        txt += f'\nId:\t{articulo["Id"]}'


    # Imprimimos los Ids de los primeros 20 articulos encontrados
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