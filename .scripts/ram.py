#!/usr/bin/env python
from subprocess import run, PIPE

def memoria():
    info_ram = run(['vmstat', '-s', '-SM'], stdout=PIPE)
    info = str(info_ram.stdout).split()
    ram_ocupada = info[5]
    return '  '+ ram_ocupada + ' MB'


ram = memoria()
print(ram)