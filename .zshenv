export PYTHONPATH="${PYTHONPATH}"
export TERM=xterm-256color
export PATH="${PATH}:${HOME}/.local/bin/:${HOME}/.config/scripts/:/usr/local/texlive/2020/bin/x86_64-linux"
export CONFIG=$HOME/.config
export SCRIPTS=$CONFIG/scripts
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
export TERMINAL=/usr/bin/alacritty
export LFS=/mnt/lfs



if [ -n "$DESKTOP_SESSION" ];then
    eval $(gnome-keyring-daemon --start)
    export SSH_AUTH_SOCK
fi

