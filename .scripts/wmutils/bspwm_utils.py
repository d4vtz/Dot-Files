#!/usr/bin/env python
from os import path
import re
import sys
import json

directorio_cmd = path.abspath(path.dirname(__file__))
sys.path.append(directorio_cmd)

from procesos import cmd_output, execute


class Escritorio:

    def __init__(self, id_escritorio):
        self.escritorio = '^' + id_escritorio

    def esta_ocupado(self):
        return cmd_output(
            f"bspc query -D -d '{self.escritorio}.occupied'") != ''

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
