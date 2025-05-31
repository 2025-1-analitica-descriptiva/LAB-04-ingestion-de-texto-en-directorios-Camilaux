import zipfile


def descomprimir_archivo(input_zip_path, output_dir):
    """
    Descomprime el archivo zip en el directorio de salida especificado.

    :param input_zip_path: Ruta al archivo zip a descomprimir.
    :param output_dir: Directorio donde se extraerán los archivos.
    """
    try:
        with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print(f"Successfully extracted {input_zip_path} to {output_dir}")
    except FileNotFoundError:
        print(f"Error: The file {input_zip_path} was not found.")
    except zipfile.BadZipFile:
        print(f"Error: {input_zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")