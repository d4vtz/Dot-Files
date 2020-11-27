#!/usr/bin/env python
import argparse
from wmutils.procesos import cmd_output

GPU = [
    'AMD Radeon R5 Graphics',
    'AMD Radeon R5 M330'
]


def parser_args():
    parser = argparse.ArgumentParser(description='Información de las GPU.')
    parser.add_argument('--gpu', '-c',
                    type=int,
                    dest='GPU',
                    help='Número de la GPU que queremos utilizar.')

    parser.add_argument('--info',
                    dest='INFORMACION',
                    help='Porcentaje de uso')
    return parser.parse_args()


def infogpu(gpu):
    info_cruda = cmd_output(f'radeontop -m -b {gpu} -l 1 -d-')
    info = info_cruda.split(',')[2:]
    tabla = {}
    i = 0
    for item in info:
        elemento = item.split()
        if i < 11:
            tabla[elemento[0]] = elemento[1]
        else:
            tabla[elemento[0]] = elemento[2] 
        i += 1
    return tabla


def vram_total(gpu):
    vram = cmd_output(
        f'cat /sys/class/drm/card{gpu}/device/mem_info_vram_total')
    return int(vram)//1048576


def temperatura(gpu):
    temperaturas = cmd_output(
        'cat /sys/class/drm/card*/device/hwmon/hwmon*/temp1_input').split('\n')
    return f'{int(temperaturas[gpu])//1000}°C'


if __name__ == '__main__':
    args = parser_args()
    if args.INFORMACION == 'gpu':
        gpu = infogpu(args.GPU)['gpu'].split('.')
        print(f'{gpu[0]}%')

    elif args.INFORMACION == 'vram':
        vram = infogpu(args.GPU)['vram'][:-2]
        vram = vram.split('.')[0]
        print(f'{vram}/{vram_total(args.GPU)} MB')

    elif args.INFORMACION == 'temp':
        print(temperatura(args.GPU))

    elif args.INFORMACION == 'nombre':
        print(GPU[args.GPU])
