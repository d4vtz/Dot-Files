#!/usr/bin/env python
from wmutils.procesos import  execute
from time import sleep

PACMAN = 'checkupdates'
AUR = 'yay -Qum'


def contar(tipo):
    lista = execute(tipo)
    contador = 0
    hay_kernel = False

    for elemento in lista:
        if '->' in elemento.split():
            contador += 1
        elif elemento.find('linux-zen') >= 0:
            hay_kernel = True
    if hay_kernel:
        return True
    else:
        return contador
        

pacman = contar(PACMAN)
aur = contar(AUR)


if pacman:
    print('Kernel Update')
else:
    total = pacman + aur
    if total == 0:
        print('Sin actualizaciones')
    elif aur != 0 and pacman == 0:
        print('AUR: {}'.format(aur))
    elif aur == 0 and pacman != 0:
        print(total)
    else:
        print('{} --> AUR: {}'.format(total, aur))
    
