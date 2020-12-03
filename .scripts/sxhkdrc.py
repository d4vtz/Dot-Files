#!/home/medicendav/Dotfiles/.scripts/env/bin/python

from os import path
from wmutils.procesos import cmd_output, rofi_lista


SXHKDRC = path.join(path.expanduser('~'), '.config/sxhkd/sxhkdrc')

def ajustar(string):
    limite = 45
    ajuste = string
    while len(ajuste) <= limite:
        ajuste += ' '
    return ajuste


def contenido(ruta):
    with open(ruta, 'r') as archivo:
        texto = archivo.read().split('\n')
    archivo.close()

    nuevo = []
    for elemento in texto:
        if elemento != '' and elemento[1] != '#' and elemento[0] != ('\t' and ' '):
            nuevo.append(elemento)

    atajos = []
    comentarios = []
    for i, item in enumerate(nuevo):
        if i % 2 == 0:
            comentarios.append(item[1:])
        else:
            atajos.append(ajustar(item))

    if len(atajos) == len(comentarios):
        cadena = ''
        for i in range(0, len(atajos)):
            cadena += atajos[i] + '\t\t' + comentarios[i] + '\n'

    return cadena

d = contenido(SXHKDRC)
a = rofi_lista(contenido(SXHKDRC).split('\n'), 'sxhkd', 15, 70)
print(a)
