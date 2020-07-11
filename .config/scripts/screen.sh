#!/bin/bash

scrot -d 1 'screen-%F-%T.png' -q 100 -e 'mv $f ~/Imágenes/Screenshots' 

