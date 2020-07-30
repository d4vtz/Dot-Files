#!/bin/bash

# Author: MeDicenDav
# https://github.com/medicendav/Dotfiles
#
#   Parametros:
#   -Puerto
#   -Silencio
#   -Subir
#   -Bajar

#Constantes
AUDIFONOS="analog-output-headphones"
ALTAVOCES="analog-output-speaker"

#Variables
PUERTO_ACTIVO=$(echo $(pactl list sinks | grep 'Puerto Activo') | awk '{print $3}')
VOLUMEN=$(echo $(pactl list sinks | grep 'Volumen') | awk '{print $5}')
SILENCIO=$(echo $(pactl list sinks | grep 'Silencio') | awk '{print $2}')



#Acciones a realizar por parametros
case $1 in
    # Cambio de puerto
    -Salida)
        if [ $PUERTO_ACTIVO == $AUDIFONOS ]; then
            pacmd set-sink-port 0 $ALTAVOCES
        else
            pacmd set-sink-port 0 $AUDIFONOS
        fi
        ;;

    # Silenciar
    -Silencio)
        amixer set Master toggle
        SILENCIO=$(echo $(pactl list sinks | grep 'Silencio') | awk '{print $2}')
        ;;    

    # Subir Volumen
    -Subir)
        amixer set Master 5%+
        VOLUMEN=$(echo $(pactl list sinks | grep 'Volumen') | awk '{print $5}')
        ;;
    
    # Vajar Volumen
    -Bajar)
        amixer set Master 5%-
        VOLUMEN=$(echo $(pactl list sinks | grep 'Volumen') | awk '{print $5}')
esac


# Mensajes de salida para Polybar
if [ $SILENCIO == "sí" ]; then
    echo 'Mute'
else
    if [ $PUERTO_ACTIVO == $AUDIFONOS ]; then
        echo '  ' $VOLUMEN
    else
        echo '  ' $VOLUMEN
    fi
fi
