#!/usr/bin/env python
from wmutils.procesos import  cmd_output, rofi

opciones = {
    '         Bloquear'  : 'i3lock-fancy',
    '         Salir'     : 'bspc quit',
    '         Hibernar'  : 'systemctl hibernate',
    '         Reiniciar' : 'reboot',
    '         Apagar'    : 'poweroff'
    }
 
respuesta = rofi(opciones, '¿Desea salir?', len(opciones), 20)
cmd_output(respuesta)
