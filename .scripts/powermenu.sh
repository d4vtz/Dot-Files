#!/bin/sh

MENU="$(rofi -sep "|" -dmenu -i -p 'Desea Salir?' -location 0 -width 25 -hide-scrollbar -line-padding 4 -padding 20 -lines 4 <<< "	   Bloquear|	   Salir|	   Reiniciar|	   Apagar")"
            case "$MENU" in
                *Bloquear) i3lock-fancy ;;
                *Salir) pkill -KILL -u medicendav ;;
                *Reiniciar) reboot ;;
                *Apagar) poweroff
            esac
