#!/usr/bin/env python
from sys import argv
import os
import datetime
from shutil import move
import pyscreenshot as ImageGrab
from time import sleep
import notify2

#pip install notify2
#pip install PIL
#pip install pyscreenshot

DESTINO = os.environ['HOME'] + '/Imágenes/Screenshots/'
RETRASO = 5


def nombre_imagen():
    date = str(datetime.datetime.now()).split()
    FECHA = date[0]
    HORA = date [1][:-7]
    return 'screen-'+ HORA + '-' + FECHA + '.png'


def screen():
    nombre = nombre_imagen()
    origen = os.getcwd() + '/' + nombre

    Screenshot = ImageGrab.grab()
    Screenshot.save(nombre)
    move(origen, DESTINO)
    notify2.init('   Captura de pantalla')
    n = notify2.Notification('\nTomada captura de pantalla')
    n.show()

def captura():
    if argv[1] == '-retraso':
        sleep(RETRASO)
        screen()
    else:
        screen()


if not os.path.exists(DESTINO):
    os.makedirs(DESTINO)
    captura()
else:
    captura()
