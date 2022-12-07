from Bio import SeqIO

# Funcion para sacar las secuencias en caso de que haya mas de una en el archivo fasta
def openFMult(dir, nucl):
    # Se trata de abrir el archivo, si no se encuentra o si el formato esta mal se le avisa al usuario y se termina el programa
    try:
        
        #Inicializamos el vector donde van a ir las secuencias
        prot=[]
        for record in SeqIO.parse(dir, "fasta"):

                # En caso de que se haya puesto el parametro -n se traducen
                if nucl:
                    prot += [record.seq.translate()]
                else:
                    prot += [record.seq]

    except FileNotFoundError:
        print('Error: No se encontró el archivo, asegurate de que hayas escrito correctamente la dirección')
        quit()
    except ValueError:
        print('Error de formato: Se encontró tu archivo, pero no se pudo abrir, asegurate de que esté en formato fasta')
        quit()

    return(prot)