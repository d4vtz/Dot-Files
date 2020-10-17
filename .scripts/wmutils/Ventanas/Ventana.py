#!/usr/bin/env python
from os import path
import re
import sys
import json
from wmutils.procesos import cmd_output
from wmutils.Ventanas.Estados import Estado


class Ventana(Estado):
    '''
    Clase que actual como contexto en la interface de
    estados de la ventana activa.
    '''
    def __init__(self):
        try:
            # id de la ventana enfocada
            self.__id_ventana = cmd_output('bspc query -N -n')
            # Estado inicial del modo de la ventana
            self.__ventana = json.loads(cmd_output(
                f'bspc query -T -n'))['client']['state']
            # Estado inicial del modo oculto de ventana
            self.__oculto = json.loads(
                cmd_output(f'bspc query -T -n'))['hidden']
            # Estado inicial del modo sticky de ventana
            self.__sticky = json.loads(
                cmd_output(f'bspc query -T -n'))['sticky']

        except Exception as __error:
            self.__id_ventana = None
            self.__ventana = None
            self.__oculto = None
            self.__sticky = None

    def modo_ventana(self) -> None:
        '''
        Método que cambia el estado del modo ventana
        '''
        try:
            self.__ventana = self.__ventana.modo_ventana()
        except Exception as _e:
            print(_e)

    def modo_oculto(self) -> None:
        '''
        Método que cambia el estado del modo ventana
        '''
        try:
            self.__oculto = self.__oculto.modo_oculto()
        except Exception as _e:
            print(_e)

    def modo_sticky(self) -> None:
        '''
        Método que cambia el estado del modo ventana
        '''
        try:
            self.__sticky = self.__sticky.modo_sticky()
        except Exception as _e:
            print(_e)

    ''' ----------  INTERFACE DE ESTADO  ---------- '''

    @property
    def estado_ventana(self) -> Estado:
        '''
        Método que obtiene el estado del modo de la ventana
        '''
        return self.__ventana

    @estado_ventana.setter
    def estado_ventana(self, status: Estado) -> None:
        '''
        Método que cambia el estado del modo de la ventana
        '''
        self.__ventana = status
        self.modo_ventana()

    @property
    def estado_oculto(self) -> Estado:
        '''
        Método que retorna el estado del modo oculto de la ventana
        '''
        return self.__oculto

    @estado_oculto.setter
    def estado_oculto(self, status: Estado) -> None:
        '''
        Método que cambia el estado oculto de la ventana
        '''
        self.__oculto = status
        self.modo_oculto()

    @property
    def estado_sticky(self) -> Estado:
        '''
        Método que retorna el estado del modo sticky de la ventana
        '''
        return self.__sticky

    @estado_sticky.setter
    def estado_sticky(self, status: Estado) -> None:
        '''
        Método que cambia el estado del modo sticky de la ventana
        '''
        self.__sticky = status
        self.modo_sticky()

    ''' ----------  INTERFACE DEL CLIENTE  ---------- '''

    @property
    def id_ventana(self) -> str:
        '''
        Método que retorna el id de la ventana.
        '''
        return self.__id_ventana

    @id_ventana.setter
    def id_ventana(self, wid: str) -> None:
        '''
        Método que cambia el id de la ventana.
        '''
        self.__id_ventana = wid

    def nombre_de_clase(self) -> list:
        '''
        Método que retorna una lista con el nombre
        de la clase de la ventana enfocada
        '''
        try:
            out = cmd_output(
                f'xprop -id {self.__id_ventana} WM_CLASS')
            return [wid.strip('"') for wid in out.split(' = ')[1].split(', ')]
        except Exception as _e:
            return []

    def dimensiones(self) -> dict:
        '''
        Método que retorna un diccionario con la geometría de la ventada
        '''
        geometry = ' '.join(cmd_output(
            f'xwininfo -metric -shape -id\
            {self.__id_ventana}').strip().split('\n')[2:8])
        regex_obj = re.search(
            r'Abs.*X.*?(-?\d+).*Abs.*Y.*?(-?\d+).*Width:\s+(\d+)\
            .*Height:\s+(\d+)',
            geometry)
        window_geometry = {
            'x_pos': int(regex_obj.group(1)),
            'y_pos': int(regex_obj.group(2)),
            'width': int(regex_obj.group(3)),
            'height': int(regex_obj.group(4))
        }
        return window_geometry

    def ventanas_ocultas(self) -> dict:
        '''
        Método que retorna un diccionario con el id y el nombre de clase
        de las ventanas ocultas
        '''
        ventanas_ocultas = cmd_output(
            'bspc query -N -n .window.hidden').split('\n')
        lista_nombres = []
        dic = {}
        for id_ventana in ventanas_ocultas:
            self.id_ventana = id_ventana
            lista_nombres.append(self.nombre_de_clase()[0])

        for id_ventana, nombre in zip(ventanas_ocultas, lista_nombres):
            dic[id_ventana] = nombre
        return dic
