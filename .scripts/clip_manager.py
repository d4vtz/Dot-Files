#!/usr/bin/env python
from os import environ
import pyperclip as clipboard
from sys import argv
from wmutils.procesos import rofi_lista

HISTORIAL = environ['HOME'] + '/.clipboard-historial'
CLIPS_MAX = 30
CLIP_LONG_MAX = 50

class Clip_Manager:

    def __init__(self):
        self.clips = []

    def lectura(self):
        try:
            with open(HISTORIAL, 'r') as historial:
                contenido = historial.read()
                historial.close()
            return contenido.split('\n')
        except:
            return []

    def copiar(self):
        contenido = self.lectura()[:-1]
        eleccion = rofi_lista(contenido, 'Clip Manager')
        clipboard.copy(eleccion)

    def escritura(self, clip):

        self.clips.reverse()
        self.clips.append(clip)
        self.clips.reverse()

        with open(HISTORIAL, 'w') as historial:
            for clip in self.clips:
                if len(clip) > 0:
                    historial.write(clip + '\n')
            historial.close()

    def demonio(self):
        while True:
            clips_historial = self.lectura()

            if CLIPS_MAX >= len(clips_historial) > 0:
                self.clips = clips_historial
            elif len(clips_historial) > CLIPS_MAX:
                self.clips = clips_historial[:CLIPS_MAX]

            clip = clipboard.paste()

            if not clip in self.clips and len(clip) < CLIP_LONG_MAX:
                self.escritura(clip)
            self.clips = []


if __name__ == '__main__':

    clip = Clip_Manager()

    if argv[1] == '-Demonio':
        clip.demonio()
    elif argv[1] == '-Copiar':
        clip.copiar()
