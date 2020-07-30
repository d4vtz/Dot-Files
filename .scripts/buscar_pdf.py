#!/bin/env python

import Busqueda as find

RUTA = '/home/medicendav/Documentos/Biblioteca/'
EXTENSIONES = [
        '.pdf',
        '.djvu'
        ]

ruta = find.buscar(EXTENSIONES, RUTA, 'Buscar libro')

zathura = [
        'zathura',          # Visualizador de documentos
        ruta                # Cadena de texto con la ruta a ejecutar
        ]
ejecutar = find.Shell(zathura)
