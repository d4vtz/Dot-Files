#!/bin/env python

from Busqueda import Busqueda


RUTA = '/home/medicendav/Documentos/Biblioteca/'
EXTENSIONES = [
        '.pdf',
        '.djvu'
        ]

ruta = Busqueda.buscar(EXTENSIONES, RUTA, 'Buscar libro')

zathura = [
        'zathura',          # Visualizador de documentos
        ruta                # Cadena de texto con la ruta a ejecutar
        ]
ejecutar = Busqueda.Shell(zathura)
