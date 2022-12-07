'''
NAME
	Articl.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez
    
DESCRIPTION
    Modulo que dado el nombre de una proteina y un tema, busca articulos donde estos 2 se mencionen.

    Regresa los primeros 3 articulos encontrados (titulo, abstract e Id), los Ids de los primeros 20 y el 
    numero total de articulos encontrados.

CATEGORY
	Gene Expression
    
USAGE
    from Articl import getArticl

    Articl(tema, protn)
'''

from Bio import Entrez
from crearTermino import crearTerm

Entrez.email = "lotmateohernandezespinosa@gmail.com"


def getArticl(tema, protn):

    # Generamos el termino de busqueda
    termino = crearTerm(tema, protn)


    # Buscamos articulos con nuestro termino y guardamos la lista de IDs 
    result = Entrez.read(Entrez.esearch(db="pubmed", term=termino))
    Ids = result['IdList']

    # Se imprime el numero de articulos encontrados de nuestro termino
    print(f'Se encontraron {result["Count"]} articulos en pubmed sobre {tema} y {protn}')

    # Si no se encontro ningun articulo se acaba el programa
    if result["Count"] == 0:
        quit()

    # Inicializamos el vector que tendra los diccionarios con los nombres, abstracts e Ids de 3 de los 
    # articulos encontrados
    Articulos = []

    # Vamos por cada uno de los primeros 3 articulos para sacar su info
    for id in Ids[0:3]:

        # Inicializamos el diccionario que tendra el nombre, abstract e Id del articulo actual
        ArtNombAbstr = {}

        # Sacamos la info del articulo actual con efetch
        articulo =  Entrez.read(Entrez.efetch(db='pubmed', id = id, api_key = '2c4f67def001c89be6a3d681c1da87fc8409'))
        
        # Guardamos el titulo
        ArtNombAbstr['Titulo'] = articulo['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle']

        # Intentamos guardar el abstract si es que tiene, si no solo guardamos 'No abstract'
        try:
            ArtNombAbstr['Abstract'] = articulo['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
       
        except:
            ArtNombAbstr['Abstract'] = 'No abstract'

        # Guardamos la Id
        ArtNombAbstr['Id'] = id


        # Guardamos este diccionario en nuestro vector
        Articulos += [ArtNombAbstr]


    # Regresamos el vector con la info de los articulos y el vector con los IDs de los demas articulos encontrados
    return(Articulos, Ids, result["Count"])


