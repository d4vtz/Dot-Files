#!/usr/bin/env python
from wmutils.procesos import cmd_output, execute


class Red:

    def escanaer(self):
        resultados = {}
        escaneo = execute('nmcli -t -f ssid,signal dev wifi list')
        for red in escaneo:
            wifi = red.split(':')
            resultados[wifi[0]] = wifi[1]
        return resultados

red = Red()
print(red.escanaer())
