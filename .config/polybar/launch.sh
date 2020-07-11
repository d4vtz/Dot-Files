#!/usr/bin/env sh

#===========================================================================
#	Agregar este archivo a tu archivo de configuración de tu wm.
#===========================================================================


# Reiniciar polybar
killall -q polybar
# Tiempo de espera para lanzar tu polybar
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Lanza tus archivos de configuración de las bar

# bar top
polybar -c ~/.config/polybar/top.ini top &
# bar down
polybar -c ~/.config/polybar/down-left.ini down-left &
polybar -c ~/.config/polybar/down-right.ini down-right &
