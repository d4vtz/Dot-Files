#!/usr/bin/env python
from sys import argv
from wmutils.bspwm_utils import  Ventana_Oculta
from wmutils.procesos import  cmd_output, rofi

if __name__ == '__main__':    

    ventana = Ventana_Oculta()
    
    if argv[1] == '-ocultar':        

        ventana.ocultar()

    elif argv[1] == '-listar_ventanas_ocultas':
        
        ventanas_ocultas = ventana.listar_ocultas()
        
        if len(ventanas_ocultas) == 1:

            ventana.id_ventana = ventanas_ocultas[0]
            ventana.mostrar()

        elif len(ventanas_ocultas) > 1:
            nombres = {}
            for id_ventana in ventanas_ocultas:
                ventana.id_ventana = id_ventana
                nombres[ventana.nombre_clase()[1]] = id_ventana
            
            if len(ventanas_ocultas) < 4:
                ventana.id_ventana = rofi(nombres, 'Ventanas ocultas', len(ventanas_ocultas), 20)
                ventana.mostrar()
            else:
                ventana.id_ventana = rofi(nombres, 'Ventanas ocultas', 4, 20)
                ventana.mostrar()
        else:
            pass
