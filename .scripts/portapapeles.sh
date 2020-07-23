#!/bin/bash

copyq copy $(copyq read 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | rofi -dmenu -i -p "Portapapeles" -theme-str '#listview {layout: vertical; lines: 12;} horibox {orientation: vertical;}')
