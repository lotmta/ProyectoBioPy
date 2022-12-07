'''
NAME
	crearTermino.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez
    
DESCRIPTION
    Modulo que crea un termino de busqueda para las herramientas Entrez. Se da el nombre de una proteina y un tema de interes.

CATEGORY
	Gene Expression
    
USAGE
    from crearTermino import crearTerm

    crearTerm(tema, protn)
'''

# Funcion para crear el termino de busqueda dado el tema de interes (cancer por ejemplo) y el nombre de nuestra proteina
def crearTerm(tema, protn):
    
    # Queremos que nuestro tema de interes y proteina este o en el titulo o en los fields
    termino = f"({tema}[Title] OR {tema}[All Fields])"
    
    termino += f" AND ({protn}[Title] OR {protn}[All Fields])" 

    # Regresamos el termino de busqueda    
    return(termino)
