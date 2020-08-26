#!/bin/env python
from os import kill
from signal import SIGTERM
from subprocess import PIPE, Popen 
from sys import argv

PROCESO = 'screenkey'

def hay_proceso(nombre):
    ps = Popen(['ps', '-e'], stdout=PIPE)
    grep = Popen(['grep', nombre], stdin=ps.stdout, stdout=PIPE)
    ps.stdout.close()
    return grep.stdout.read().decode()


def main():
    if argv[1] == '-mensaje':
        if hay_proceso(PROCESO):
            print('     ')
        else:
            print('   ')
    if argv[1] == '-conmutador':
        if hay_proceso(PROCESO):
            lineas = hay_proceso(PROCESO).split('\n')[:-1]
            for linea in lineas:
                pid = linea.split()[0]
                kill(int(pid), SIGTERM)
        else:
            Popen(PROCESO)


main()