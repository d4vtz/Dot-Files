#!/usr/bin/env bash  
source ~/.cache/wal/colors.sh 

echo -e "[options]\n
allow_bold = true\n
audible_bell = true\n
bold_is_bright = true\n
clickable_url = true\n
dynamic_title = true\n
font = Iosevka Nerd Font 9\n
fullscreen = true\n
#icon_name = terminal\n
mouse_autohide = true\n
scrollback_lines = 10000\n
urgent_on_bell = true\n
\n
# $BROWSER is used by default if set, with xdg-open as a fallback\n
browser = xdg-open\n
\n
# "system", "on" or "off"\n
cursor_blink = system\n
\n
# "block", "underline" or "ibeam"\n
cursor_shape = ibeam\n
\n
# ====================================\n
[colors]\n
\n
foreground=   $foreground\n
background=   $background\n
cursor=       $cursor\n
\n
color0=       $color0\n
color1=       $color1\n
color2=       $color2\n
color3=       $color3\n
color4=       $color4\n
color5=       $color5\n
color6=       $color6\n
color7=       $color7\n
color8=       $color8\n
color9=       $color9\n
color10=      $color10\n
color11=      $color11\n
color12=      $color12\n
color13=      $color13\n
color14=      $color14\n
color15=      $color15" > ~/.config/termite/config




echo -e "include "/home/medicendav/.gtkrc-2.0.mine"
gtk-theme-name="Adapta-Nokto"
gtk-icon-theme-name="Tela-manjaro"
gtk-font-name="Comfortaa 10"
gtk-cursor-theme-name="capitaine-cursors-light"
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_ICONS
gtk-toolbar-icon-size=GTK_ICON_SIZE_MENU
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=1
gtk-enable-input-feedback-sounds=1
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle="hintmedium"" > ~/.gtkrc-2.0

gtk-update-icon-cache
