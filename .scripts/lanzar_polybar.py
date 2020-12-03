#!/usr/bin/env python
from os import kill, environ
from signal import SIGTERM
from subprocess import DEVNULL, PIPE, Popen
from time import sleep

PROCESO = 'polybar'
polybar = [
    ['polybar', '-c', environ['HOME']+'/.config/polybar/top.ini', 'top'],
]


def hay_proceso(nombre):
    ps = Popen(['ps', '-e'], stdout=PIPE)
    grep = Popen(['grep', nombre], stdin=ps.stdout, stdout=PIPE)
    ps.stdout.close()
    return grep.stdout.read().decode()


if __name__ == '__main__':
    if hay_proceso(PROCESO):
        lineas = hay_proceso(PROCESO).split('\n')[:-1]
        for linea in lineas:
            pid = linea.split()[0]
            kill(int(pid), SIGTERM)
    sleep(2)

    for barra in polybar:
        Popen(barra, stdout=DEVNULL, stderr=DEVNULL)
