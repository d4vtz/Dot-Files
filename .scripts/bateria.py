#!/usr/bin/env python
import notify2
from time import sleep
from wmutils.procesos import cmd_output


def notificar():
    icon = "gtk-ok"
    time_out = 1000
    title = "Mensaje de prueba"
    description = "Bateria critica... Conecte por favor"

    try:
        notify2.init("wee-notifier")
        wn = notify2.Notification(title, description, icon)
        wn.set_urgency(notify2.URGENCY_CRITICAL)
        wn.set_timeout(time_out)
        wn.show()
        sleep(10)
    except Exception as error:
        pass


class Bateria:

    def __init__(self):
        estado = cmd_output('acpi -V').split('\n')
        self.carga = int(estado[0].split()[3][:-2])
        self.conectada = estado[2].split()[2] == 'on-line'
        self.completa = self.carga >= 99

    def estado_critico(self):
        return self.carga < 30

    def nivel(self):
        if 80 <= self.carga < 100:
            return ''
        elif 60 <= self.carga < 80:
            return ''
        elif 40 <= self.carga < 60:
            return ''
        elif 20 <= self.carga < 40:
            return ''
        elif 0 <= self.carga < 20:
            return ''
        else:
            return ''



if __name__ == '__main__':
    bateria = Bateria()

    if bateria.conectada:
        print(f'   {bateria.carga}%')

    elif bateria.completa:
        print('   Carga completa')

    else:
        if bateria.estado_critico():
            print(f'{bateria.nivel()}  {bateria.carga}%')
            notificar()
        else:
            print(f'{bateria.nivel()}  {bateria.carga}%')
