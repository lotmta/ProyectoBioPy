# ProyectoBioPy

## Objetivo

En este proyecto se desarrolló una herramienta cuya función es realizar una investigación en la base de datos de NCBI, dada una proteína desconocida realiza una búsqueda BLAST para identificarla. Una vez identificada, dado el nombre de una enfermedad se realiza una búsqueda de artículos en los que se establece una asociación entre la enfermedad y dicha proteína ya identificada.

## Diseño

Para el diseño de la herramienta se dividió el código en dos partes principales. El programa principal se encuentra en la carpeta "src" bajo el nombre de "InfProt.py", mientras que los módulos que serán llamados por el programa principal se encuentran en la carpeta "módulos", dentro de "src". Los módulos utilizados son: "Articl.py","blastSearch.py","crearTermino.py","openFile.py","openFileMultiple.py","write.py".

A continuación se explica brevemente la función de cada módulo dentro del programa principal.

Articl.py: Modulo que dado el nombre de una proteína y un tema, busca artículos donde estos 2 se mencionen. Regresa los primeros 3 artículos encontrados (titulo, abstract e Id), los Ids de los primeros 20 y el numero total de artículos encontrados. blastSearch.py: Modulo que corre blastp dada una secuencia proteica. Regresa el nombre de la proteína con el mejor alineamiento crearTermino.py:Modulo que crea un termino de búsqueda para las herramientas Entrez. Se da el nombre de una proteína y un tema de interés. openFile.py: Función abre el archivo de entrada con la secuencia y la traduce de no ser una secuencia proteica. openFileMultiple.py: Esta función realiza el mismo proceso que la anterior pero para múltiples secuencias. write.py:Modulo que escribe un archivo con los datos dados por los demás módulos

## Resultados

El desarrollo de la herramienta fue éxitoso, a continuación se muestra el formato en que se imprime el resultado de las búsquedas. [![Captura de pantalla (20)](https://user-images.githubusercontent.com/100377560/206542304-b8fbd92d-dda1-439b-9b2b-1487fdeaee36.png)](https://user-images.githubusercontent.com/100377560/206542304-b8fbd92d-dda1-439b-9b2b-1487fdeaee36.png)

Además, en el repositorio se encuentran dos archvivos output de InfProt, uno que contiene el resultado de blastp llamado "BlastOutpt.txt" y otro con los artículos encontrados por la búsqueda en NCBI llamado "Outpt.txt". En el archivo "Output.txt" se muestra el nombre de la proteína identificada, el tema de interés requerido, el número de artículos encontrados que establecen una relación entre ambos, el título de los primeros tres encontrados y los Ids de los siguientes veinte.

## Conclusiones

InfProt permite, dados los resultados de una extracción de proteoma o RNA-seq, obtener información publicada en la literatura de NCBI que asocie la proteína caracterizada y algún tema de interés, como puede ser una enfermedad. Esto resulta útil para realizar hipótesis sobre el fenotipo de células que se encuentren sobre expresando una proteína a priori desconocida.


