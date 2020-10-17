#!/usr/bin/env python
from wmutils.procesos import cmd_output
from abc import ABC, abstractmethod


class Estado(ABC):
    '''
    Clase Abstracta Estado
    Contiene métodos abstractos para cambiar de estado
    la ventana
    '''

    @abstractmethod
    def modo_ventana(self) -> None:
        '''
        Método que controla el modo de la ventana
        - Pantalla completa
        - Mosaico
        - Flotante
        '''

    @abstractmethod
    def modo_oculto(self) -> None:
        '''
        Método que controla el modo oculto de la ventana
        - Oculto_On
        - Oculto_Off
        '''

    @abstractmethod
    def modo_sticky(self) -> None:
        '''
        Método que controla el modo sticky de la ventana
        - Sticky_On
        - Sticky_Off
        '''


class PantallaCompleta(Estado):
    '''
    Clase que cambia de estado el modo de la ventana a Pantalla completa.
    '''

    def modo_ventana(self) -> Estado:
        '''
        Método que cambia la ventana a modo pantalla completa.
        '''
        cmd_output('bspc node -t fullscreen')
        return 'fullscreen'

    def modo_oculto(self):
        ''' No hace nada '''

    def modo_sticky(self):
        ''' No hace nada '''


class Mosaico(Estado):
    '''
    Clase que cambia de estado el modo de la ventana a modo Mosaico.
    '''

    def modo_ventana(self) -> Estado:
        '''
        Método que cambia la ventana a modo mosaico.
        '''
        cmd_output('bspc node -t tiled')
        return 'tiled'

    def modo_oculto(self):
        ''' No hace nada '''

    def modo_sticky(self):
        ''' No hace nada '''


class Flotante(Estado):
    '''
    Clase que cambia de estado el modo de la ventana a modo flotante.
    '''

    def modo_ventana(self) -> Estado:
        '''
        Método que cambia la ventana a modo flotante.
        '''
        cmd_output('bspc node -t floating')
        return 'floating'

    def modo_oculto(self):
        ''' No hace nada '''

    def modo_sticky(self):
        ''' No hace nada '''


class Ocultar_On(Estado):
    '''
    Clase que cambia el estado de la ventana a modo oculto.
    '''
    def __init__(self, id_ventana):
        self.__id_ventana = id_ventana

    def modo_ventana(self):
        ''' No hace nada '''

    def modo_oculto(self) -> Estado:
        '''
        Método que cambia la ventana a modo oculto.
        '''
        cmd_output(f'bspc node {self.__id_ventana} -g hidden=on')
        return 'true'

    def modo_sticky(self):
        ''' No hace nada '''


class Ocultar_Off(Estado):
    '''
    Clase que desactiva el estado de la ventana en modo oculto.
    '''

    def __init__(self, id_ventana):
        self.__id_ventana = id_ventana

    def modo_ventana(self):
        ''' No hace nada '''

    def modo_oculto(self) -> Estado:
        '''
        Método que desactiva la ventana del modo oculto.
        '''
        cmd_output(f'bspc node {self.__id_ventana} -g hidden=off')
        return 'false'

    def modo_sticky(self):
        ''' No hace nada '''


class Sticky_On(Estado):
    '''
    Clase que cambia el estado de la ventana a modo sticky.
    '''

    def modo_oculto(self):
        ''' No hace nada '''

    def modo_ventana(self):
        ''' No hace nada '''

    def modo_sticky(self) -> Estado:
        '''
        Método que cambia la ventana a modo sticky.
        '''
        cmd_output(f'bspc node -g sticky=on')
        return 'true'


class Sticky_Off(Estado):
    '''
    Clase que desactiva el estado de la ventana del modo sticky.
    '''

    def modo_oculto(self):
        ''' No hace nada '''

    def modo_ventana(self):
        ''' No hace nada '''

    def modo_sticky(self) -> Estado:
        '''
        Método que desactiva la ventana del modo sticky.
        '''
        cmd_output(f'bspc node -g sticky=off')
        return 'false'
