# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
from pathlib import Path

from homework.descomprimir_archivo import descomprimir_archivo
from homework.save_csv import save_csv

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # Descomprimir el archivo input.zip en la carpeta input
    
    # Decompress input.zip to the repository root
    input_zip_path = Path("files/input.zip")
    output_dir = Path("files/input")
    if not output_dir.exists():
        descomprimir_archivo(input_zip_path, output_dir)
    
    # Crear la carpeta output si no existe
    output_dir = Path("files/output")
    output_dir.mkdir(exist_ok=True)
    
    # Inicializar listas para almacenar los datos
    train_data = []
    test_data = []

    # Función para procesar los archivos de un directorio
    def process_directory(directory, dataset):
        for sentiment in ['positive', 'negative', 'neutral']:
            sentiment_dir = Path(directory/sentiment)
            if sentiment_dir.exists():
                for file_path in sentiment_dir.glob('*.txt'):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        phrase = file.read().strip()
                        dataset.append({'phrase': phrase, 'target': sentiment})

    # Procesar los directorios de entrenamiento y prueba
    train_dir = Path('files/input/input/train')
    test_dir = Path('files/input/input/test')
    if train_dir.exists():
        process_directory(train_dir, train_data)
    if test_dir.exists():
        process_directory(test_dir, test_data)

    # Guardar los datos en archivos CSV 

    return save_csv(output_dir, train_data, test_data)

print(pregunta_01())


