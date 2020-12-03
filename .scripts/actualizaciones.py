#!/usr/bin/env python

#  Autor: MedicenDav
#  Dotfiles: github.com/medicendav/Dotfiles
from sys import argv
from bs4 import BeautifulSoup
import requests
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


def huerfanos():
    paquetes = cmd_output('pacman -Qtdq').split('\n')
    if paquetes[0] == '':
        return 0
    else:
        return len(paquetes)


def noticias():
    url = 'https://www.archlinux.org'
    pagina = requests.get(url, timeout=5)
    contendo = BeautifulSoup(pagina.content, 'html.parser')
    titulo = contendo.find_all('a')[16].text
    fecha = contendo.find_all('p', class_='timestamp')[0]
    fecha = str(fecha.text).split('-')
    fecha = f'{fecha[2]}/{fecha[1]}/{fecha[0]}'

    return (fecha, titulo)


if argv[1] == '-PACMAN':
    pacman = contar(PACMAN)
    print(pacman)
elif argv[1] == '-AUR':
    aur = contar(AUR)
    print(aur)

elif argv[1] == '-huerfanos':
    print(huerfanos())

elif argv[1] == '-noticias':
    titulo = noticias()[1]
    print(titulo)

elif argv[1] == '-fecha':
    fecha = noticias()[0]
    print(fecha)
