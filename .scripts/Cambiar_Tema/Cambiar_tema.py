#!/usr/bin/env python
import os
import sys
from subprocess import PIPE, DEVNULL, Popen
import Tema

HOME = os.environ['HOME']
GTKRC2 = HOME + '/.gtkrc-2.0'
GTKRC3 = HOME + '/.config/gtk-3.0/settings.ini'
RUTA_WALL = HOME +'/.config/wallpapers/'
EXTENSION = [
    '.jpg',
    '.png'
]

def escanear(extensiones, directorio):

    resultados = {}
    for directorio_actual, carpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            (nombre, extension) = os.path.splitext(archivo)
            if extension in extensiones:
                resultados[nombre] = os.path.join(directorio_actual,
                                                  archivo)
    return resultados


def generar_lista(archivos):

    cadena = ''
    for archivo in archivos:
        cadena += archivo + '\n'
    cadena = cadena[:-1]
    return cadena


def buscar(extensiones, ruta):

    resultados = escanear(extensiones, ruta)
    cadena = generar_lista(resultados.keys())
    echo = [
        'echo',                     # Imprimir en shell
        '-e',                       # Mantiene los caracteres \n
        cadena                      # Cadena de texto
        ]
    rofi = [
        'rofi',                     # Lanzador de aplicaciones
        '-lines', '10',             # Lineas a mostrar
        '-width', '20',             # Anchura del menu
        '-location', '3',           # Localización
        '-dmenu',                   # Tipo de menu
        '-p', 'Selecciona un tema'  # Titulo
        ]

    ECHO = Popen(echo, stdout=PIPE)
    ROFI = Popen(rofi, stdin=ECHO.stdout, stdout=PIPE)
    ECHO.stdout.close()
    resultado = ROFI.stdout.read().decode()[:-1]
    return resultados.get(resultado)



def leer_archivo(ruta):
    archivo = open(ruta, 'r')
    lineas = []
    for linea in archivo:
        lineas.append(linea)
    archivo.close()

    return lineas


def buscar_cadena(cadena, archivo):
    for linea in archivo:
        if linea.find(cadena) >= 0:
            return linea


def lineas_a_remplazar(lista, archivo):
    lineas = []
    for elemento in lista:
        lineas.append(buscar_cadena(elemento, archivo))
    return lineas


def editar(tema, gtk = 2):
    editado = []
    if gtk == 2:
        archivo = leer_archivo(GTKRC2)
    else:
        archivo = leer_archivo(GTKRC3)

    remplazos = lineas_a_remplazar(tema.keys(), archivo)

    for linea in archivo:
        if linea in remplazos:
            for elemento in tema.keys():
                if linea.find(elemento) >= 0:
                    if gtk == 2:
                        editado.append(elemento + '="' + tema.get(elemento) + '"\n')
                    else:
                        editado.append(elemento + '=' + tema.get(elemento) + '\n')
        else:
            editado.append(linea)
    return editado

def reescribir_archivo(lista,ruta):
    archivo = open(ruta, 'w')
    for elemento in lista:
        archivo.write(elemento)
    archivo.close()


def tema_dark(imagen):
    if imagen.find(RUTA_WALL + 'Dark') >= 0:
        return True
    else:
        return False


if __name__ == '__main__':
    wallpaper = buscar(EXTENSION, RUTA_WALL)
    if tema_dark(wallpaper):

        gtk2 = editar(Tema.Dark)
        gtk3 = editar(Tema.Dark, 3)
        reescribir_archivo(gtk2, GTKRC2)
        reescribir_archivo(gtk3, GTKRC3)
    else:

        gtk2 = editar(Tema.Light)
        gtk3 = editar(Tema.Light, 3)
        reescribir_archivo(gtk2, GTKRC2)
        reescribir_archivo(gtk3, GTKRC3)

    Popen(['wal', '-i', wallpaper], stdout=DEVNULL)
