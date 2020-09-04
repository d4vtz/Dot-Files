#!/usr/bin/env python
from subprocess import Popen, PIPE

lista = [
    '             Bloquear',
    '             Salir',
    '             Hibernar',
    '             Reiniciar',
    '             Apagar'
]

cadena = ''
for elemento in lista:
    cadena += elemento + '\n'
cadena = cadena[:-1]

echo = [
    'echo',
    '-e',
    cadena
    ]

rofi = [
    'rofi',
    '-lines', '4',
    '-width', '25',
    '-location', '0',
    '-dmenu',
    '-p', '¿Desea salir?'
    ]

Echo = Popen(echo, stdout=PIPE)
Rofi = Popen(rofi, stdin=Echo.stdout, stdout=PIPE)
Echo.stdout.close()
respuesta = Rofi.stdout.read().decode()[:-1].strip()

if respuesta == 'Bloquear':
    Popen('i3lock-fancy')
elif respuesta == 'Salir':
    Popen(['pkill', '-KILL', '-u', 'medicendav'])
elif respuesta == 'Reiniciar':
    Popen('reboot')
elif respuesta == 'Apagar':
    Popen('poweroff')
elif respuesta == 'Hibernar':
    Popen(['systemctl', 'hibernate'])
