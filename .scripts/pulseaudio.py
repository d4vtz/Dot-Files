#!/usr/bin/env python

# Author: MeDicenDav
# https://github.com/medicendav/Dotfiles
#
#   Parametros:
#   -Puerto
#   -Silencio
#   -Subir
#   -Bajar
#   -Polybar

from sys import argv
from pulsectl import Pulse
from subprocess import PIPE, DEVNULL, Popen

XOBPIPE = '/tmp/xobpipe'
AUDIFONOS = 'analog-output-headphones'
ALTAVOCES = 'analog-output-speaker'
SINK_ID = 0


def datos(entrada):
    xob = open(XOBPIPE, 'w')
    xob.write(entrada + '\n')
    xob.close()



if __name__ == '__main__':
    pulse = Pulse()
    sink = pulse.sink_list()[SINK_ID]
    puerto_activo = sink.port_active.name
    volumen = round(sink.volume.value_flat * 100)
    hay_mute = sink.mute == 1

    if len(argv) == 2:
        if argv[1] == '-Puerto':
            if puerto_activo == ALTAVOCES:
                pulse.port_set(sink, AUDIFONOS)
            else:
                pulse.port_set(sink, ALTAVOCES)

        elif argv[1] == '-Silencio':
            if hay_mute:
                pulse.mute(sink, mute=False)
                datos('!')

            else:
                pulse.mute(sink)
                datos('')

        elif argv[1] == '-Subir':
            if volumen < 150:
                pulse.volume_change_all_chans(sink, +0.05)
                volumen = round(sink.volume.value_flat * 100)
                datos(str(volumen))

        elif argv[1] == '-Bajar':
            pulse.volume_change_all_chans(sink, -0.05)
            volumen = round(sink.volume.value_flat * 100)
            datos(str(volumen))

        elif argv[1] == '-Polybar':
            volumen = round(sink.volume.value_flat * 100)
            if not hay_mute:
                if puerto_activo == ALTAVOCES:
                    print('   {}%'.format(volumen))
                else:
                    print('   {}%'.format(volumen))
            else:
                print('Mute')
