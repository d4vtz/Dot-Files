#!/usr/bin/env python
from wmutils.procesos import cmd_output


def memoria():
    info_ram = cmd_output('vmstat -s -SM')
    info = info_ram.split('\\n')
    ram_ocupada = info[0]
    ram_total = info[1]
    return f'{ram_ocupada}/{ram_total} MB'


ram = memoria()
print(ram)
