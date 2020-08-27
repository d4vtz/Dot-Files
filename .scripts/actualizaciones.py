#!/bin/env python
from subprocess import PIPE, DEVNULL, run
from time import sleep

PACMAN = ['checkupdates']
AUR = ['yay', '-Qum']


def contar(tipo):
    update = run(tipo, stdout=PIPE, stderr=DEVNULL)
    sleep(3)
    lista = str(update.stdout).split()
    contador = 0
    for elemento in lista:
        if elemento == '->':
            contador += 1
    return contador

def hay_kernel():
    update = run(PACMAN, stdout=PIPE, stderr=DEVNULL)
    sleep(2)
    lista = str(update.stdout).split()
    for elemento in lista:
        if elemento.find('linux-zen') >= 0:
            return True
        
        

pacman = contar(PACMAN)
aur = contar(AUR)


if not hay_kernel():
    total = pacman + aur
    if total == 0:
        print('Sin actualizaciones')
    elif aur != 0 and pacman == 0:
        print('AUR: {}'.format(aur))
    elif aur == 0 and pacman != 0:
        print(total)
    else:
        print('{} --> AUR: {}'.format(total, aur))
else:
    print('Kernel Update')
