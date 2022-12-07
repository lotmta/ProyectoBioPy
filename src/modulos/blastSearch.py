'''
NAME
	blastSearch.py
    
VERSION
    1.0
    
AUTHOR
	Aldo Garcia	
    
DESCRIPTION
    Modulo que corre blastp dada una secuencia proteica. Regresa el nombre de la proteina con el mejor alineamiento

CATEGORY
	Gene Expression
    
USAGE
    from blastSearch import protName

    protName(protSeq)
'''

from Bio import SearchIO
from Bio.Blast import NCBIWWW

def protName(protSeq):

    # Corremos blastp, usando la base de datos pdb y pidiendo solo el mejor hit
    print('Corriendo Blastp...')
    result = NCBIWWW.qblast("blastp", "pdb", protSeq, hitlist_size=1)
    
    # Parseamos el resultado para poder trabajar con el
    result = SearchIO.read(result, 'blast-xml')


    # Sacamos el nombre de la proteina con la que tuvo el mejor hit
    protNomb = result[0].description


    # Por la forma en la que pdb nombra las proteinas, aveces tienen cosas antes y despues del nombre de 
    # la proteina (como el organismo del que es) por lo que las quitamos usando try ya que no siempre estan 
    # y si no estuvieran daria out of index error
    try:
        protNomb = protNomb.split(',')[1]
    except:
        pass

    protNomb = protNomb.split('[')[0]


    # Se imprime a pantalla el nombre del mejor hit y el E value de la alineacion
    print(f"Tu proteina tuvo el mejor alienamiento con {protNomb}, con un E value de {result[0][0].evalue}")

    # Regresamos el nombre probable de nuestra proteina
    return(protNomb)
