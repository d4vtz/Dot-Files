#                                                                            
#        	       Mi configurción de zsh                  
#                          By:CallmeDav 



#		Aplicar esquema de colores de pywal
#################################################################
export TERM=xterm-256color
(/usr/bin/cat /home/medicendav/.cache/wal/sequences &)
source /home/medicendav/.cache/wal/colors-tty.sh

export PATH="${PATH}:${HOME}/.local/bin/:${HOME}/.config/scripts/"
export PATH
export CONFIG=$HOME/.config
export SCRIPTS=$CONFIG/scripts
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

#	Configurando mi prompt en  ~/.p10k.zsh.
#################################################################

source /home/medicendav/.config/powerlevel10k/powerlevel10k.zsh-theme
[[ ! -f /home/medicendav/.p10k.zsh ]] || source /home/medicendav/.p10k.zsh

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi


#################################################################
#
#	     Mis funciones
#	     By:CallmeDav


extraer(){
    EXTENSION=$([[ "$1" = *.* ]] && echo "${1#*.}")

	case "$EXTENSION" in

	tar)    
	echo "Extrayendo $1 ..."
	echo ""
	tar -xvf $1
	echo "Extracción finalizada";;

	gz)    
	echo "Extrayendo $1 ..."
	echo ""
	gzip -d $1
	echo "Extracción finalizada";;

	bz2)    
	echo "Extrayendo $1 ..."
	echo ""
	bzip2 -d $1
	echo "Extracción finalizada";;

	tar.gz)    
	echo "Extrayendo $1 ..."
	echo ""
	tar -xzvf $1
	echo "Extracción finalizada";;

	tar.bz2)    
	echo "Extrayendo $1 ..."
	echo ""
	bzip2 -dc $1 | tar -xv
	echo "Extracción finalizada";;

	zip)    
	echo "Extrayendo $1 ..."
	echo ""
	unzip $1
	echo "Extracción finalizada";;

	rar)    
	echo "Extrayendo $1 ..."
	echo ""
	unrar x $1
	echo "Extracción finalizada";;
	esac

}



#"""""""""""""""""""""""""""""""""""""""""""""""""
#    -- Crear una carpeta y entrar a ella --
#"""""""""""""""""""""""""""""""""""""""""""""""""

mkcd(){
	mkdir $1
	cd $1
}

#""""""""""""""""""""""""""""""""""""""""""""""""
#  -- Entra a una carpeta y lista su contenido--
#""""""""""""""""""""""""""""""""""""""""""""""""

cl(){
	cd $1
	ls
}

#""""""""""""""""""""""""""""""""""""""""""""""""
#  -- Entra a una carpeta y lista su contenido --
#""""""""""""""""""""""""""""""""""""""""""""""""

script(){
	touch $1.sh && sudo chmod +x $1.sh
	echo '#!/bin/bash' > $1.sh 
	vim $1.sh
}


#""""""""""""""""""""""""""""""""""""""""""""""""
#  --            Repositorio git               --
#""""""""""""""""""""""""""""""""""""""""""""""""

enlace(){
    DIR=$HOME/Dotfiles
    echo "Moviendo arcivo a Dotfiles"
    mv $1 $DIR/$1
    echo "Creando enlace simbolico"
	ln -s $DIR/"$1" ~/$1
    echo "Cambiando al directorio $DIR"
    cd $DIR
    echo "Añadiendo al repositorio"
    git add $1
    echo "Regresando al directorio principal"
    cd
}

    commit(){
    echo "Cambiando al directorio $DIR"
    cd $DIR
    echo "Agregando commit"
    git commit -m "$*"
    echo "Regresando al directorio principal"
    cd
}



#       Generando mi historial de comandos
#################################################################

SAVEHIST=1000
HISTFILE=/home/medicendav/.zsh_history






#################################################################
#							
#			  Mis alias			
#			By: CallmeDav


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#            --  lsd Esteroides para mi ls  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias ll='lsd -lha --group-dirs=first'
alias ls='lsd --group-dirs=first'
alias cat='bat --paging=never'


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#		       --  tmux  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias attach='tmux attach'
alias temux='tmux new -s'


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#		     --  Sistema  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias bye='pkill -KILL -u medicendav'
alias rmc='rm -r'
alias cpr='cp-r'
alias class='xprop WM_CLASS'
alias brillo='./.config/scripts/brillo.sh'
alias wpa='sudo wpa_supplicant -B -i wlp2s0 -c /etc/wpa_supplicant/wpa_supplicant-wlp2s0.conf'


alias vim='nvim'
alias bspwmrc='nvim ~/.config/bspwm/bspwmrc'
alias sxhkdrc='nvim ~/.config/sxhkd/sxhkdrc'
alias zshrc='nvim ~/.zshrc'
alias init.vim='nvim ~/.config/nvim/init.vim'


alias py='python'
alias Tex='tllocalmgr'

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#		      --  pacman  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""





#################################################################
#							
#			  Mis plugins			
#			By: CallmeDav

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# To customize prompt, run `p10k configure` or edit ~/Dotfiles/.p10k.zsh.
[[ ! -f ~/Dotfiles/.p10k.zsh ]] || source ~/Dotfiles/.p10k.zsh
