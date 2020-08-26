#!/usr/bin/env python
from subprocess import run, PIPE, DEVNULL
from sys import argv



if len(argv) > 1:
    try:
        ventana = run(  
            'xdo id -N '+ argv[1] + ' || xdo id -n '+argv[1],
            check=True,
            shell=True,
            stdout=PIPE,
        )
    
        id = str(ventana.stdout)[2:-3]
        hay_id = True
    except:
        ejecutable = argv[2]
        hay_id = False        

    if not hay_id:
        run(ejecutable, stdout=DEVNULL, stderr=DEVNULL)
    else:
        ids = id.split('\\n')
        for id in ids:
            try:
                run(
                    'bspc node '+ id +' --flag hidden --to-monitor focused --focus',
                    check=True,
                    shell=True,
                )
            except:
                continue
