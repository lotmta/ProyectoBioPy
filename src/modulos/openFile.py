from Bio import SeqIO

def openF(dir, nucl):
    # Se trata de abrir el archivo, si no se encuentra o si el formato esta mal se le avisa al usuario y se termina el programa
    try:
        prot = SeqIO.read(dir, "fasta")
        if nucl:
            prot = prot.translate()

    except FileNotFoundError:
        print('Error: No se encontró el archivo, asegurate de que hayas escrito correctamente la dirección')
        quit()
    except ValueError:
        print('Error de formato: Se encontró tu archivo, pero no se pudo abrir, asegurate de que esté en formato fasta')
        quit()

    # En caso de que se haya usado -n se traduce la secuencia
    return(prot)