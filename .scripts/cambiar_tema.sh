#!/usr/bin/env bash  
source ~/.cache/wal/colors.sh 

echo -e "[options]
allow_bold = true
audible_bell = true
bold_is_bright = true
clickable_url = true
dynamic_title = true
font = Iosevka Nerd Font 9
fullscreen = true
#icon_name = terminal
mouse_autohide = true
scrollback_lines = 10000
urgent_on_bell = true

# $BROWSER is used by default if set, with xdg-open as a fallback
browser = xdg-open

# "system", "on" or "off"
cursor_blink = system

# "block", "underline" or "ibeam"
cursor_shape = ibeam

# ====================================
[colors]

foreground=   $foreground
background=   $background
cursor=       $cursor

color0=       $color0
color1=       $color1
color2=       $color2
color3=       $color3
color4=       $color4
color5=       $color5
color6=       $color6
color7=       $color7
color8=       $color8
color9=       $color9\
color10=      $color10
color11=      $color11
color12=      $color12
color13=      $color13
color14=      $color14
color15=      $color15" > ~/.config/termite/config

#0c1216

if [ "$background" == '#081550' ]; then

echo -e "# DO NOT EDIT! This file will be overwritten by LXAppearance.
# Any customization should be done in ~/.gtkrc-2.0.mine instead.

include \"/home/medicendav/.gtkrc-2.0.mine\"
gtk-theme-name=\"tarde-de-olas\"
gtk-icon-theme-name=\"Tela-manjaro\"
gtk-font-name=\"Comfortaa 10\"
gtk-cursor-theme-name=\"capitaine-cursors-light\"
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle=\"hintmedium\"" > ~/.gtkrc-2.0

echo -e "[Settings]
gtk-theme-name=tarde-de-olas
gtk-icon-theme-name=Tela-manjaro
gtk-font-name=Comfortaa 10
gtk-cursor-theme-name=capitaine-cursors-light
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle=hintmedium
gtk-xft-rgba=rgb
" > ~/.config/gtk-3.0/settings.ini

elif [ "$background" == '#0c1216' ]; then

echo -e "# DO NOT EDIT! This file will be overwritten by LXAppearance.
# Any customization should be done in ~/.gtkrc-2.0.mine instead.

include \"/home/medicendav/.gtkrc-2.0.mine\"
gtk-theme-name=\"Pentagono\"
gtk-icon-theme-name=\"McMojave-circle\"
gtk-font-name=\"Comfortaa 10\"
gtk-cursor-theme-name=\"capitaine-cursors-light\"
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle=\"hintmedium\"" > ~/.gtkrc-2.0

echo -e "[Settings]
gtk-theme-name=Pentagono
gtk-icon-theme-name=McMojave-circle
gtk-font-name=Comfortaa 10
gtk-cursor-theme-name=capitaine-cursors-light
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle=hintmedium
gtk-xft-rgba=rgb
" > ~/.config/gtk-3.0/settings.ini


else

echo -e "# DO NOT EDIT! This file will be overwritten by LXAppearance.
# Any customization should be done in ~/.gtkrc-2.0.mine instead.

include \"/home/medicendav/.gtkrc-2.0.mine\"
gtk-theme-name=\"Adapta-Nokto\"
gtk-icon-theme-name=\"ePapirus\"
gtk-font-name=\"Comfortaa 10\"
gtk-cursor-theme-name=\"capitaine-cursors-light\"
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle=\"hintmedium\"" > ~/.gtkrc-2.0

echo -e "[Settings]
gtk-theme-name=Adapta-Nokto
gtk-icon-theme-name=ePapirus
gtk-font-name=Comfortaa 10
gtk-cursor-theme-name=capitaine-cursors-light
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle=hintmedium
gtk-xft-rgba=rgb
" > ~/.config/gtk-3.0/settings.ini

fi

pkill -KILL -u medicendav
