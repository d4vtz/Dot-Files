#!/bin/bash
mkdir -p ~/Imágenes/Screenshots/

if [ "$1" == -retraso ]; then
    scrot -d 1 'screen-%F-%T.png' -q 100 -e 'mv $f ~/Imágenes/Screenshots/'; sleep 1; notify-send 'Tomada captura de pantalla'
 else
    scrot 'screen-%F-%T.png' -q 100 -e 'mv $f ~/Imágenes/Screenshots/'; notify-send 'Tomada captura de pantalla'
fi


