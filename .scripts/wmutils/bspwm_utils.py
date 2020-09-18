#!/usr/bin/env python
from os import path
import re
import sys
import json

directorio_cmd = path.abspath(path.dirname(__file__))
sys.path.append(directorio_cmd)

from procesos import cmd_output, execute


class Ventana:

    def __init__(self):
        self.__id_ventana = cmd_output("bspc query -N -n '.window.focused'")

    @property
    def id_ventana(self):
        return self.__id_ventana 

    @id_ventana.setter
    def id_ventana(self, ventana):
        self.__id_ventana = ventana

    @staticmethod
    def lista_de_ventanas():
        return execute('bspc query -N')

    def pid(self):
        output = cmd_output(f'xprop -id {self.__id_ventana} _NET_WM_PID')
        if output:
            return output.split(' = ')[1]
        else:
            return ''

    def nombre_clase(self):
        try:
            out = cmd_output(f'xprop -id {self.__id_ventana} WM_CLASS')
            wm_class = [wid.strip('"') for wid in out.split(' = ')[1].split(', ')]
            return wm_class
        except Exception:
            return []

    def modo_fullscreen(self):
        return cmd_output(
            f'bspc query -N -n {self.__id_ventana}.fullscreen') != ''

    def modo_floating(self):
        return cmd_output(
            f'bspc query -N -n {self.__id_ventana}.floating') != ''

    def win_geometry(self):
        window_geometry = ' '.join(cmd_output(
        f'xwininfo -metric -shape -id {self.__id_ventana}').strip().split(
        '\n')[2:8])
        regex_obj = re.search(
        r'Abs.*X.*?(-?\d+).*Abs.*Y.*?(-?\d+).*Width:\s+(\d+).*Height:\s+(\d+)',
        window_geometry)
        window_geometry = {
            'x_pos': int(regex_obj.group(1)),
            'y_pos': int(regex_obj.group(2)),
            'width': int(regex_obj.group(3)),
            'height': int(regex_obj.group(4))
        }
        return window_geometry

    def hacer_pagajosa(self):
        return cmd_output(f'bspc node {self.__id_ventana} -g sticky') != ''

    def es_pegajosa(self):
        return cmd_output(f'bspc query -T -n {self.__id_ventana}') != ''


class Ventana_Oculta(Ventana):

    def __init__(self):
        Ventana.__init__(self)
        self.esta_oculta = cmd_output(
            f'bspc query -N -n {self.id_ventana}.hidden') != ''

    @staticmethod
    def listar_ocultas():
        return execute('bspc query -N -n .window.hidden')

    def ocultar(self):
        cmd_output(f'bspc node {self.id_ventana} -g hidden=on')

    def mostrar(self):
        cmd_output(f'bspc node {self.id_ventana} -g hidden=off --focus')

    def mostrar_en_escritorio_enfocado(self):
        cmd_output(
        'bspc node {self.id_ventana} --flag hidden=off --to-monitor focused --focus')

class Escritorio:

    def __init__(self, id_escritorio):
        self.escritorio = '^' + id_escritorio

    def esta_vacio(self):
        return cmd_output(
            f"bspc query -D -d '{self.escritorio}.occupied'") == ''

    def modo_monocle(self):
        return json.loads(cmd_output(
            f'bspc query -T -d {self.escritorio}'))['layout'] == 'monocle'

    def hay_ventanas_pegajosas(self):
        return cmd_output(
            f"bspc query -N -d {self.escritorio} -n '.window.sticky'") != '' 


class Monitor:

    def __init__(self, nombre_monitor=None):
        self.nombre_monitor = nombre_monitor

    def dim_pantalla(self):
        dimensiones = cmd_output('xrandr --listactivemonitors')
        if self.nombre_monitor is None:
            dimensiones = '\n'.join(dimensiones.split('\n'))

        busqueda = re.search((
            '' if self.nombre_monitor is None else self.nombre_monitor) +
                r'\s+(\d{3,4})/\d+x(\d{3,4})',
                dimensiones,
                flags=re.MULTILINE)
        screen_dim = {
            'width': int(busqueda.group(1)),
            'height': int(busqueda.group(2))
        }
        return screen_dim
