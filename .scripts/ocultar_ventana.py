#!/usr/bin/env python

#  Autor: MedicenDav
#  Dotfiles: github.com/medicendav/Dotfiles

#  Uso: ocultar_ventana.py [-h] [--ocultar] [--listar]
#  Argumentos opcionales:

#  -h, --help  Mostrar este mensaje y salir
#  --ocultar   Ocultar ventana enfocada.
#  --listar    Listar ventanas ocultas.

from argparse import ArgumentParser
from wmutils.procesos import cmd_output, rofi
from wmutils.Ventanas.Estados import Ocultar_Off, Ocultar_On
from wmutils.Ventanas.Ventana import Ventana


def parseArguments():
    # Función que pasa los argumentos con ayuda del
    # modulo argparse
    parser = ArgumentParser()

    parser.add_argument('--ocultar',
                        dest='OCULTAR',
                        action='store_true',
                        help='Ocultar ventana enfocada.'
                        )

    parser.add_argument('--listar',
                        dest='LISTA',
                        action='store_true',
                        help='Listar ventanas ocultas.'
                        )
    return parser.parse_args()


# Paso los argumentos a la variable args y
# creo una instancia de la clase ventana.
args = parseArguments()
ventana = Ventana()


if args.OCULTAR:
    # Oculto la ventana enfocada.
    ventana.estado_oculto = Ocultar_On(ventana.id_ventana)

elif args.LISTA:
    # Obtengo un diccionario con el id y nombre de clase
    # de las ventanas ocultas.
    ventanas_ocultas = ventana.ventanas_ocultas()
    id_ventana = rofi(ventanas_ocultas, 'Que ventana desea mostrar?')
    ventana.estado_oculto = Ocultar_Off(id_ventana)
