'''
NAME
	InfProt.py
    
VERSION
    2.0
    
AUTHOR
	Lot, Andres, Aldo	
    
DESCRIPTION
    Dada la secuencia de una proteína desconocida y un tema en el que se quiere ver si tiene algún rol, da el nombre
    probable de la proteína dada usando blastp, y los artículos donde se menciona esta proteína y el tema.

    Se puede usar si al hacer un estudio de proteoma en células cancerosas, por ejemplo, se ve que una proteína de la
    cual no se sabe su nombre o función es sobre expresada.

CATEGORY
	Gene Expression
    
USAGE
    py InfProt.py -f (Direccion del archivo) -t (Tema de interes)
    py InfProt.py -f (Direccion del archivo) -t (Tema de interes) -BS (Si se quiere que se escriba un archivo con los detalles del blastp) 
'''

import sys
import argparse

sys.path.insert(0, '.\src\modulos')

from blastSearch import protName
from Articl import getArticl
from write import wrFile
from openFile import openF
from openFileMultiple import openFMult

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con la secuencia",
                    required=True)
parser.add_argument('-BS', "--BlastSave",
                    help="Usa este parametro si quieres que guarden los detalles del blastp en un archivo",
                    default=False,
                    action='store_true')
parser.add_argument("-t", "--topic",
                    help="Introduce el tema en el que quieres ver si tu proteina es relevante, cancer por ejemplo",
                    required=True)
parser.add_argument('-n', "--nucleotide",
                    help="Usa este parametro si tu secuencia es de ADN o RNA",
                    default=False,
                    action='store_true')
args = parser.parse_args()



prots = openFMult(args.file, args.nucleotide)
im = len(prots)


i=0
while i < im:

    prot = prots[i]

    # Pasamos el tema elegido a una variable
    tema = args.topic

    # Usamos la funcion que corre blast para encontrar el nombre (probable) de nuestra proteina
    protN = protName(prot, args.BlastSave, i)

    # Buscamos los articulos donde este nuestro tema y nuestra proteina
    articulos, Ids, NumArts = getArticl(tema, protN)

    # Con todo lo obtenido escribimos el archivo de salida
    wrFile(protN, tema, articulos, Ids, NumArts, i)

    i+=1
