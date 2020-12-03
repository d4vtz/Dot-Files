#!/usr/bin/env python
from wmutils.procesos import cmd_output

padding_simple = 2
padding_conky = cmd_output('cat ~/.config/bspwm/bspwmrc | grep right_padding').split()
padding_conky = padding_conky[3]

if __name__ == '__main__':
    padding = cmd_output('bspc config right_padding')
    if padding == padding_conky:
        cmd_output(f'bspc config right_padding {padding_simple}')
    else:
        cmd_output(f'bspc config right_padding {padding_conky}')
