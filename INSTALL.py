#!/usr/bin/env python
from os import path, environ, mkdir, getcwd, symlink
from time import sleep

HOME = environ['HOME']
CONFIG = HOME + '/.config'
DOTFILES = getcwd()

CARPETAS = [
    '/.config/alacritty',
    '/.config/bspwm',
    '/.config/Code - OSS',
    '/.config/dunst',
    '/.config/gtk-3.0',
    '/.config/nvim',
    '/.config/picom',
    '/.config/polybar',
    '/.config/ranger',
    '/.config/redshift',
    '/.config/rofi',
    '/.config/spicetify',
    '/.config/sxhkd',
    '/.config/termite',
    '/.config/wallpapers',
    '/.config/zathura',
    '/.mpd',
    '/.ncmpcpp',
    '/.python',
    '/.scripts',
    '/.themes',
    '/.gtkrc-2.0',
    '/.p10k.zsh',
    '/.vimrc',
    '/.Xresources',
    '/.zshenv',
    '/.zshrc',
]


if __name__ == '__main__':
    print('  ------------------------------------------------------  ')
    print('    Script de instalación de mi configuración de BSPWM    ')
    print('  ------------------------------------------------------  ')
    print('')
    print('')

    if not path.exists(CONFIG):
        print(f'Creando directorio: {CONFIG}...')
        mkdir(CONFIG)
        print('Hecho')

    print('  ------------------------------------------------------  ')
    print('Creando los enlaces simbólicos')
    print(f'Directorio actual: {DOTFILES}')

    for carpeta in CARPETAS:
        DESTINO = HOME + '/Prueba' + carpeta
        ORIGEN = DOTFILES + carpeta

        print(f'Creando enlace simbólico de {carpeta}')
        print(f'{DESTINO} --> {ORIGEN}')
        symlink(ORIGEN, DESTINO)
        print(f'Echo... Archivo de configuración {carpeta} instalado')
        print('')
        sleep(3)

    print('  ------------------------------------------------------------  ')
    print('    Finalización de instalación de mi configuración de BSPWM    ')
    print('  ------------------------------------------------------------  ')
