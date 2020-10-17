#!/usr/bin/env python

#  Autor: MedicenDav
#  Dotfiles: github.com/medicendav/Dotfiles

from wmutils.procesos import cmd_output

# Comandos para mostrar paquetes a actualizar.
PACMAN = 'checkupdates'
AUR = 'yay -Qum'


def update_kernel():
    # Comprueba si hay actualización del kernel.
    lista = cmd_output(PACMAN).split('\n')
    for elemento in lista:
        if 'linux-zen' in elemento.split():
            return True


def contar(tipo):
    # Retorna el número de paquetes a actualizar.
    lista = cmd_output(tipo).split('\n')
    contador = 0
    for elemento in lista:
        if '->' in elemento.split():
            contador += 1
    return contador


pacman = contar(PACMAN)
aur = contar(AUR)
total = pacman + aur

if total == 0:
    print('Sin actualizaciones')
elif aur != 0 and pacman == 0:
    print(f'AUR: {aur}')
elif aur == 0 and pacman != 0:
    if update_kernel():
        print('Update kernel')
    else:
        print(total)
else:
    print(f'{total} --> AUR: {aur}')
