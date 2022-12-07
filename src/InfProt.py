import sys
from Bio import Entrez, SeqIO
import argparse

sys.path.insert(0, '.\src\modulos')


parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con la secuencia",
                    required=True)
parser.add_argument('-BS', "BlastSave",
                    help="Usa este parametro si quieres que guarden los detalles del blastp en un archivo",
                    default=False,
                    action='store_true')
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
