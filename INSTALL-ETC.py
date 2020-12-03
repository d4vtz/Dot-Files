#!/usr/bin/env python
from os import path, environ, mkdir, getcwd, symlink
from time import sleep
import shutil

DOTFILES = getcwd()

ETC = [
    '/etc/default/grub',
    '/etc/X11/xorg.config.d/50-synaptics.conf',
    '/etc/makepkg.conf',
    '/etc/pacman.conf',
]


if __name__ == '__main__':
    print('  ------------------------------------------------------  ')
    print('        Script de instalación de mis archivos /etc        ')
    print('  ------------------------------------------------------  ')
    print('')
    print('')

    print('  ------------------------------------------------------  ')
    print('Creando los enlaces simbólicos')
    print(f'Directorio actual: {DOTFILES}')

    for archivo in ETC:
        DESTINO = archivo
        ORIGEN = DOTFILES + archivo

        if path.exists(archivo):
            print(f'Encontrado archivo {archivo}')
            print('Renombrendo archivo como {}'.format(archivo + '.backup'))
            shutil.move(archivo, archivo + '.backup')
            print('Echo')

        print(f'Creando enlace simbólico de {archivo}')
        print(f'{DESTINO} --> {ORIGEN}')
        symlink(ORIGEN, DESTINO)
        print(f'Echo... Archivo de configuración {archivo} instalado')
        print('')
        sleep(3)

    print('  ------------------------------------------------------------  ')
    print('           Script de instalación de mis archivos /etc           ')
    print('  ------------------------------------------------------------  ')
