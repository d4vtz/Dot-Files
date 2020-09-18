#!/usr/bin/env python
from wmutils.procesos import cmd_output


class Bateria:

    def __init__(self):
        self.estado = cmd_output('acpi -b').split()
    
    def carga(self):
        return int(self.estado[3][:-2])
    
    def esta_conectada(self):
        return self.estado[2][:-1] == 'Charging'
    
    def esta_cargada(self):
        return self.estado[2][:-1] == 'Full'

    def estado_critico(self):
        return self.carga() < 10

    def nivel(self):
        if 80 <= self.carga() < 100:
            return 4
        elif 60 <= self.carga() < 80:
            return 3
        elif 40 <= self.carga() < 60:
            return 2
        elif 20 <= self.carga() < 40:
            return 1
        elif 0 <= self.carga() < 20:
            return 0
        else:
            return 5



imagen = ['', '', '', '', '', '']

if __name__ == '__main__':
    bateria = Bateria()
    
    if bateria.esta_conectada():
        print(f'   {bateria.carga()}%')
    
    elif bateria.esta_cargada():
        print('   Carga completa')
    
    else:
        print(f'{imagen[bateria.nivel()]}  {bateria.carga()}%')
