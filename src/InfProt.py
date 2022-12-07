'''
NAME
	InfProt.py
    
VERSION
    1.0
    
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
from Bio import Entrez, SeqIO
import argparse

sys.path.insert(0, '.\modulos')

from blastSearch import protName
from Articl import getArticl
from write import wrFile

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
args = parser.parse_args()

Entrez.email = "lotmateohernandezespinosa@gmail.com"


 # Se trata de abrir el archivo, si no se encuentra o si el formato esta mal se le avisa al usuario y se termina el programa
try:
    prot = SeqIO.read(args.file, "fasta")

except FileNotFoundError:
    print('Error: No se encontró el archivo, asegurate de que hayas escrito correctamente la dirección')
    quit()
except ValueError:
    print('Error de formato: Se encontró tu archivo, pero no se pudo abrir, asegurate de que esté en formato fasta')
    quit()

# Pasamos el tema elegido a una variable
tema = args.topic

# Usamos la funcion que corre blast para encontrar el nombre (probable) de nuestra proteina
print('Corriendo Blastp...')
protN = protName(prot.seq)

# Buscamos los articulos donde este nuestro tema y nuestra proteina
articulos, Ids, NumArts = getArticl(tema, protN)

# Con todo lo obtenido escribimos el archivo de salida
wrFile(protN, tema, articulos, Ids, NumArts)
