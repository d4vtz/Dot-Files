#!/usr/bin/env bash

# Author: Sophie Bernadin-Mercier
# https://github.com/Shuhala/i3blocks-colorscheme-picker
#
# Inspired by i3blocks-shutdown_menu
# https://github.com/vivien/i3blocks-contrib/blob/master/shutdown_menu/shutdown_menui
#
# Modified by vide0hanz
#
# Requires pywal and rofi

###   CONFIG NOTES   ###
#  -location  
#0 = center
#1 = top left 
#2 = top center
#3 = top right
#4 = middle right
#5 = bottom right
#6 = bottom center
#7 = bottom left 
#8 = middle left

###   Assign wallpapers directory here   ###

wallpapers_dir=$HOME/.config/wallpapers/

###   Config   ###

pywal_options=(-i)
rofi_title="Set Wallpaper + Theme"
rofi_options=(
	-width 25 \
	-location 5 \
	-bw 2 \
	-dmenu -i \
	-p "${rofi_title}" "${rofi_colors}" \
	-lines 10
#	-kb-cancel F7 ##assign key value if desired for rofi toggle menu, must be setup in main config file
)

###   Display menu   ###

typeset -A menu
for file in $(find $wallpapers_dir -type f -regex '.*\(jpg\|png\)$'); 
do
	file_name=${file##*/}
	menu[${file_name%%.*}]=$file
done

launch_rofi=(rofi "${rofi_options[@]}")
selection="$(printf '%s\n' "${!menu[@]}" | sort | "${launch_rofi[@]}")"

###    Apply selected wallpaper   ###

if [ ! -z $selection ]; then
	exec `wal -i "${menu[${selection}]}" -o ~/.config/scripts/termite_config_theme.sh -t`
stop
fi

