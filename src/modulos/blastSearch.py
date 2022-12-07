'''
NAME
	blastSearch.py
    
VERSION
    1.2
    
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
import io

def protName(protSeq, BS, i):

    # Corremos blastp, usando la base de datos pdb y pidiendo solo el mejor hit
    print('Corriendo Blastp...')

    # En caso de que se haya usado el parametro para guardar el resultado de Blast, guardamos todos los alineamientos
    if BS:
        result = NCBIWWW.qblast("blastp", "pdb", protSeq)
    else:
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

    # En caso de que se haya usado el parametro para guardar el resultado de blast, lo guardamos en un archivo
    if BS:

        # Se hace esto por si hay mas de una secuencia en el fasta
        if i == 0:
            file = io.open("BlastOutpt.txt", "w", encoding='utf-8')
        else:
            file = io.open(f"BlastOutpt_{i+1}.txt", "w", encoding='utf-8')
        
        txt= 'Blast Results:\n\n'

        for alignment in result:
            txt +=f"Sequence ID: {alignment.id}"
            txt +=f"\nDescription: {alignment.description}"
            txt +=f"\nE value: {alignment[0].evalue}"
            txt +=f"\nBit Score:  {alignment[0].bitscore}"
            txt +=f"\nAlignment:\n{alignment[0].aln}\n\n"
        
        file.write(txt)
        file.close()

    # Regresamos el nombre probable de nuestra proteina
    return(protNomb)