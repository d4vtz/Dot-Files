#!/usr/bin/env python
from os import path, walk
import sys


def escanear(extensiones, directorio):
    """
    Función que escanea los archivos encontrados
    en un directorio.

    Parametros:
        - extensiones: list
        Una lista con las extensiones de archivo a escanear.
        - directorio: str
        Un directorio pasado por cadena de texto.

    Return: dic
        - Un diccionario el el cual se guardan como llave los nombres
        de ficheros y como clave su ruta completa.
    """

    resultados = {}
    for directorio_actual, carpetas, archivos in walk(directorio):
        for archivo in archivos:
            (nombre, extension) = path.splitext(archivo)
            if extension in extensiones:
                resultados[nombre] = path.join(directorio_actual,
                                                  archivo)
    return resultados
