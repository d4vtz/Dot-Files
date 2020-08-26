#!/usr/bin/env python
from subprocess import run, PIPE, DEVNULL

CLASE = 'Spotify'

def id_ventana():
    try:
        ventana = run(  
            'xdo id -N '+CLASE+' || xdo id -n '+CLASE,
            check=True,
            shell=True,
            stdout=PIPE,
            stderr=DEVNULL
        ) 
        return str(ventana.stdout)[2:-3].split('\\n')
    except:
        return None


def hay_ventana():
    if id_ventana() is not None:
        return True
    else:
        return False


if __name__ == '__main__':
    if hay_ventana():
        for id in id_ventana():
            try:
                run(
                    'bspc node '+ id +' --flag hidden --to-monitor focused --focus',
                    check=True,
                    shell=True,
                )
            except:
                continue
