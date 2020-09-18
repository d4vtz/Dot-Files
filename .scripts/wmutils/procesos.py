#!/usr/bin/env python
from subprocess import Popen, run, PIPE, DEVNULL


def cmd_output(cmd):
    output = run(
             cmd,
             stdout=PIPE,
             stderr=DEVNULL,
             shell=True,
             text=True
    )
    if output.returncode == 0:
        return output.stdout[:-1]
        #return popen.stdout[:-1].split('\n')
    else:
        return ''


def execute(cmd):
    popen = run(
            cmd,
            stdout=PIPE,
            stderr=DEVNULL,
            shell=True,
            text=True,
            )
    if popen.returncode == 0:
        return popen.stdout[:-1].split('\n')
    else:
        return []


def pipes(cmd_input, cmd_output):
    try:
        Input = Popen(
                cmd_input,
                stdout=PIPE,
                shell=True,
                text=True
                )
        Output = Popen(
                 cmd_output,
                 stdin=Input.stdout,
                 stdout=PIPE,
                 shell=True,
                 text=True
                )
        return Output.stdout.read()[:-1]
    except Exception:
        return ''


def rofi(diccionario, titulo, lineas = 10, width = 25):
    cadena = '\n'.join(diccionario.keys())
    respuesta = pipes(
        "echo -e '{}'".format(cadena),
        f'rofi -lines {lineas} -width {width} -location 0 -dmenu -p ' + '"' + titulo + '"'
        )
    return diccionario.get(respuesta)


def rofi_lista(lista, titulo, lineas = 10, width = 25):
    cadena = '\n'.join(lista)
    respuesta = pipes(
        "echo -e '{}'".format(cadena),
        f'rofi -lines {lineas} -width {width} -location 0 -dmenu -p ' + '"' + titulo + '"'
        )
    return respuesta