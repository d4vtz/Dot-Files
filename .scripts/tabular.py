#!/usr/bin/env python
from argparse import ArgumentParser
from wmutils.procesos import cmd_output, rofi


def parseArguments():
    parser = ArgumentParser()

    parser.add_argument('--agregar',
                        dest='DIR',
                        help='Agregar ventana del lado DIR a la pestaña con la ventana enfocda.'
                        )

    parser.add_argument('--eliminar',
                        dest='DEL',
                        action='store_true',
                        help='Eliminar ventana con ID de la pestaña'
                        )

    parser.add_argument('--listar',
                        dest='LIST',
                        action='store_true',
                        help='Listar ventanas tabuladas.'
                        )
    return parser.parse_args()


COLOR_1 = '#111111'
COLOR_2 = '#7A7777'
COLOR_3 = '#8F8E24'
COLOR_4 = '#FFFFFF'

TABBED_CONFIG = f"-c -k -o '{COLOR_1}' -O '{COLOR_2}' -t '{COLOR_3}' -T '{COLOR_4}'"


# Agregar ventana enfocada a una instancia con pestañas en la dirección dada
def obtener_wid(direccion):
    direcciones = {
        'left': 'west',
        'up': 'north',
        'right': 'east'
    }
    return cmd_output(f'bspc query -N -n {direcciones[direccion]}')


# Obtener wid de la ventana raíz
def obtener_root_wid():
    return cmd_output('xwininfo -root | grep "Window id"').split()[3]


def obtener_clientes(wid):
    children = cmd_output(f'xwininfo -id {wid} -children')
    lista = children.split('\n')[6:]

    ventana = []
    wid = []
    for elemento in lista:
        ventana.append(elemento.split())

    for elemento in ventana:
        for i in range(len(elemento)):
            if i == 0:
                wid.append(elemento[i])
    return wid


def obtener_clase(wid):
    return cmd_output(
        f'xprop -id {wid} | grep "WM_CLASS"').split()[2][1:-2]


if __name__ == '__main__':
    args = parseArguments()

    if args.DIR is not None:

        ventana_padre = cmd_output('bspc query -N -n focused')
        ventana_hija = obtener_wid(args.DIR)
        pestañas = cmd_output('tabbed {} -d'.format(TABBED_CONFIG))

        if obtener_clase(ventana_hija) != '':
            if pestañas != '':
                cmd_output(f'xdotool windowreparent {ventana_hija} {pestañas}')
                cmd_output(f'xdotool windowreparent {ventana_padre} {pestañas}')

    elif args.DEL:
        ventana_enfocada = cmd_output('bspc query -N -n focused')
        clientes = obtener_clientes(ventana_enfocada)
        for cliente in clientes:
            cmd_output(f'xdotool windowreparent {cliente} {obtener_root_wid()}')

    elif args.LIST:
        ventana_enfocada = cmd_output('bspc query -N -n focused')
        lista_pestaña = obtener_clientes(ventana_enfocada)
        lista = [obtener_clase(elemento) for elemento in lista_pestaña]
        dic = {}
        for i in range(len(lista)):
            dic[lista[i]] = lista_pestaña[i]
        eleccion = rofi(dic, 'Pestañas')
        cmd_output(f'xdotool windowfocus {eleccion}')
