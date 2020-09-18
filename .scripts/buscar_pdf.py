#!/bin/env python
from wmutils.procesos import cmd_output, rofi
from Busqueda import escanear

RUTA = '/home/medicendav/Documentos/Biblioteca/'
EXTENSIONES = ['.pdf', '.djvu']


if __name__ == '__main__':

        resultados = escanear(EXTENSIONES, RUTA)
        ruta_pdf = rofi(resultados, 'Selecciona un libro')
        cmd_output(f'zathura {ruta_pdf}')
