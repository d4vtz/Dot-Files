#!/usr/bin/env python
from os import kill, environ
from signal import SIGTERM
from subprocess import DEVNULL, PIPE, Popen 
from sys import argv
from time import sleep

PROCESO = 'redshift'


def hay_proceso(nombre):
    ps = Popen(['ps', '-e'], stdout=PIPE)
    grep = Popen(['grep', nombre], stdin=ps.stdout, stdout=PIPE)
    ps.stdout.close()
    return grep.stdout.read().decode()
    

if __name__ == '__main__':
    if len(argv) >= 2:
        if hay_proceso(PROCESO):

            lineas = hay_proceso(PROCESO).split('\n')[:-1]
            for linea in lineas:
                pid = linea.split()[0]
                kill(int(pid), SIGTERM)
        else:
            Popen(PROCESO, stdin=DEVNULL)
        
    else:
        if hay_proceso(PROCESO):
            print('盛     ')
        else:
            print('盛     ')

