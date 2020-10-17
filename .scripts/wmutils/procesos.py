#!/usr/bin/env python
from subprocess import Popen, run, PIPE, DEVNULL


def cmd_output(cmd: str) -> str:
    output = run(
             cmd,
             stdout=PIPE,
             stderr=DEVNULL,
             shell=True,
             text=True
    )
    if output.returncode == 0:
        return output.stdout[:-1]
    else:
        return ''


def pipes(cmd_input: str, cmd_output: str) -> str:
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


def rofi(diccionario: dict,
         titulo: str,
         lineas: int = 10,
         width: int = 25
        ) -> str:

    cadena = '\n'.join(diccionario.values())
    respuesta = pipes(
        "echo -e '{}'".format(cadena),
        f'rofi -lines {lineas} -width {width} -location 0 -dmenu -p ' +
        '"' + titulo + '"'
        )
    for llave, clave in diccionario.items():
        if clave == respuesta:
            return llave
