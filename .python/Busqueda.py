#!/usr/bin/env python
import os
import sys
from subprocess import PIPE, Popen


class Shell:
    """
    Crea un objeto, el cual ejecuta un comando de shell.

    Atributos:
        - comando:
            Recibe una lista, con los comandos y parametos de shell a
            ejecutar.
        - ejecutar:
            Llama a la funcion Popen del modulo subprocess y ejecuta
            el comando
            pasado por parametro a la instancia creada.
        - salida:
            Obtiene la salida estándar del comando a ejecutar.
        - error:
            Obtiene el error estándar del comando a ejecutar.
        -entrada:
            Pasa la entrada estándar del comando a ejecutar

    """
    def __init__(self, comando):
        self.comando = comando
        self.ejecutar = Popen(self.comando, stdout=PIPE, stderr=PIPE)
        self.salida = self.ejecutar.stdout
        self.error = self.ejecutar.stderr
        self.entrada = self.ejecutar.stdin

    def salida(self):
        """
        salida: Método que retorna la salida estándar
        o el error estándar depende del caso,
        con ayuda del método formato.

        """
        if not self.error:
            return self.formato(self.salida)
        else:
            return self.formato(self.error)

    def formato(self, mensaje):
        """
        formato: Método que retorna una cadena de texto, formateada
        de modo que elimina los caracteres de formato inicial y final
        que devuelve el comando ejecutado.

        """
        return str(mensaje)[2:-3]

    def tuberia(self, salida):
        """
        tuberia: Método que toma la salida de un proceso y lo manda
        como entrada a otro proceso.
        Retorna la salida del segundo proceso.

        """
        proceso_salida = Popen(salida, stdin=self.salida, stdout=PIPE)
        self.ejecutar.stdout.close()

        output, error = proceso_salida.communicate()
        if not error:
            return str(output)[2:-3]
        else:
            return str(error)[2:-3]


#   Funciones
def escanear(extensiones, directorio):
    """
    Función que escanea los archivos encontrados
    en un directorio.

    Parametros:
        - extensiones: list
        Una lista con las extensiones de archivo a escanear.
        - directorio: str
        Un directorio pasado por cadena de texto.

    Return: dic
        - Un diccionario el el cual se guardan como llave los nombres
        de ficheros y como clave su ruta completa.
    """

    resultados = {}
    for directorio_actual, carpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            (nombre, extension) = os.path.splitext(archivo)
            if extension in extensiones:
                resultados[nombre] = os.path.join(directorio_actual,
                                                  archivo)
    return resultados


def generar_lista(archivos):
    """
    Función que retorna una cadena de texto formateada de manera
    que pueda ser procesada por el interprete de shell.

    Parametros:
        - archivos: list
        Una lista de archivos generada por la función escanear.

    Return: str
        - Una cadena de texto.
    """
    cadena = ''

    for archivo in archivos:
        cadena += archivo + '\n'
    cadena = cadena[:-1]
    return cadena


def buscar(extensiones, ruta, titulo_rofi):
    """
    Función que retorna toma como entrada una ruta a scanear, junto con
    una lista de extensiones a buscar, el titulo que rofi muestra al
    ejecutarse y retorna la ruta absoluta del archivo seleccionado.

    Parametros:
        - extensiones: list
        Una lista de cadenas con las extensiones, por ejemplo ['.pdf'].
        - ruta: str
        Una cadena de texto con la ruta a escanear, '/home/$user/*.pdf'
        - titulo: str
        Una cadena con el titulo de rofi.

    Return: str
    - Una cadena de texto.
    """

    resultados = escanear(extensiones, ruta)
    cadena = generar_lista(resultados.keys())
    echo = [
        'echo',                     # Imprimir en shell
        '-e',                       # Mantiene los caracteres \n
        cadena                      # Cadena de texto
        ]
    rofi = [
        'rofi',                     # Lanzador de aplicaciones
        '-lines', '10',             # Lineas a mostrar
        '-width', '50',             # Anchura del menu
        '-location', '0',           # Localización
        '-dmenu',                   # Tipo de menu
        '-p', titulo_rofi           # Titulo
        ]

    ECHO = Shell(echo)
    resultado = ECHO.tuberia(rofi)
    return resultados.get(resultado)
