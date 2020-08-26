#!/usr/bin/env python
from os import environ
import pyperclip as clipboard
from sys import argv
from subprocess import Popen, PIPE

HISTORIAL = environ['HOME'] + '/.clipboard-historial'

class Clip_Manager:

    def __init__(self):
        open(HISTORIAL, "w+").close()
    
    def clip_rofi(self):

        cadena = ''
        for clip in self.lectura():
            cadena += clip + '\n'
        cadena = cadena[:-1]

        echo = [
            'echo',
            '-e',
            cadena
            ]

        rofi = [
            'rofi',
            '-lines', '10',
            '-width', '50',
            '-location', '0',
            '-dmenu',
            '-p', 'Clip Manager'
            ]

        Echo = Popen(echo, stdout=PIPE)
        Rofi = Popen(rofi, stdin=Echo.stdout, stdout=PIPE)
        Echo.stdout.close()

        return Rofi.stdout.read().decode()[:-1]
        
    def copiar(self):
        texto = self.clip_rofi()
        clipboard.copy(texto)
    
    def lectura(self):
        contenido = []
        with open(HISTORIAL, 'r') as historial:
            for linea in historial.readlines():
                contenido.append(linea)
        return contenido

    def escritura(self, texto):
        with open(HISTORIAL, 'w+') as historial:
            if len(texto) == 1:
                historial.write('\n'.join(texto))
            else:
                historial.write(texto[0])

    def demonio(self):
        while True:
            clip = clipboard.paste()
            clips = self.lectura()
            if clip not in clips:
                clips.append(clip)
                clips.reverse()
                self.escritura(clips)




clip = Clip_Manager()
if argv[1] == '-Demonio':
    clip.demonio()

elif argv[1] == '-Copiar':
    #clip.copiar()
    print(clip.lectura())
