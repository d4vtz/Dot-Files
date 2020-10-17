#!/usr/bin/env python

#  Autor: MedicenDav
#  Dotfiles: github.com/medicendav/Dotfiles

from wmutils.procesos import cmd_output, rofi

# Diccionario con los comandos a ejecutar
opciones = {
    'i3lock-fancy': '         Bloquear',
    'bspc quit': '         Salir',
    'systemctl hibernate': '         Hibernar',
    'reboot': '         Reiniciar',
    'poweroff': '         Apagar'
    }

# Lanzar rofi para elegir la opción.
respuesta = rofi(opciones, '¿Desea salir?', len(opciones), 20)
cmd_output(respuesta)
