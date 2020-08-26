#!/bin/env python

# Author: MeDicenDav
# https://github.com/medicendav/Dotfiles
#
#   Parametros:
#   -Puerto
#   -Silencio
#   -Subir
#   -Bajar


from subprocess import PIPE, Popen, run 
from sys import argv

AUDIFONOS = 'analog-output-headphones'
ALTAVOCES = 'analog-output-speaker'


def grep(palabra_clave, numero_palabra):
    pactl = Popen(['pactl', 'list', 'sinks'], stdout=PIPE)
    grep = Popen(['grep', palabra_clave], stdin=pactl.stdout, stdout=PIPE)
    pactl.stdout.close()
    return grep.stdout.read().decode().split()[numero_palabra-1]


def hay_sonido():
    if grep('Silencio', 2) == 'no':
        return True
    else:
        return False


def parametros():
    if argv[1] == '-Puerto':
        if grep('Puerto Activo', 3) == ALTAVOCES:
            run(['pacmd', 'set-sink-port', '0', AUDIFONOS], stdout=PIPE)
        else:
            run(['pacmd', 'set-sink-port', '0', ALTAVOCES], stdout=PIPE)

    elif argv[1] == '-Silencio':
        run(['amixer', 'set', 'Master', 'toggle'], stdout=PIPE)

    elif argv[1] == '-Subir':
        run(['amixer', 'set', 'Master', '5%+'], stdout=PIPE)

    elif argv[1] == '-Bajar':
        run(['amixer', 'set', 'Master', '5%-'], stdout=PIPE)


def main():
    if len(argv) == 2:
        parametros()
    if hay_sonido:
        if grep('Puerto Activo', 3) == ALTAVOCES:
            print('   {}'.format(grep('Volumen', 5)))
        else:
            print('   {}'.format(grep('Volumen', 5)))
    else:
        print('Mute')


main()