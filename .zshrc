#
#        	       Mi configurción de zsh
#                          By:CallmeDav


# Plugins
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-command-no-found/zsh-command-no-found.zsh
source /usr/share/zsh/plugins/zsh-sudo/zsh-sudo.zsh





#		Aplicar esquema de colores de pywal
#################################################################
export TERM=xterm-256color
(/usr/bin/cat /home/medicendav/.cache/wal/sequences &)
source /home/medicendav/.cache/wal/colors-tty.sh

#	Configurando mi prompt desde ~/.p10k.zsh.
#################################################################
# Habilitar Powerlevel10k
source /home/medicendav/.config/powerlevel10k/powerlevel10k.zsh-theme
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi



# Promt personalizado, ejecutar 'p10k configure' o editar ~/.p10k.zsh
[[ ! -f /home/medicendav/.p10k.zsh ]] || source /home/medicendav/.p10k.zsh

#       Generando mi historial de comandos
#################################################################
# Ignorar comandos repetidos del historial, compartir historial
setopt histignorealldups sharehistory
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=/home/medicendav/.zsh_history



# Habilitar el autocompletado
#################################################################
autoload -Uz compinit
compinit

zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'


# Importando fzf
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
#################################################################
#
#	     Mis funciones
#	     By:CallmeDav

# Man en colores
function man() {
    env \
    LESS_TERMCAP_mb=$'\e[01;31m' \
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    man "$@"
}


# fzf improvement
function fzf-lovely(){

	if [ "$1" = "h" ]; then
		fzf -m --reverse --preview-window down:20 --preview '[[ $(file --mime {}) =~ binary ]] &&
 	                echo {} is a binary file ||
	                 (bat --style=numbers --color=always {} ||
	                  highlight -O ansi -l {} ||
	                  coderay {} ||
	                  rougify {} ||
	                  cat {}) 2> /dev/null | head -500'

	else
	        fzf -m --preview '[[ $(file --mime {}) =~ binary ]] &&
	                         echo {} is a binary file ||
	                         (bat --style=numbers --color=always {} ||
	                          highlight -O ansi -l {} ||
	                          coderay {} ||
	                          rougify {} ||
	                          cat {}) 2> /dev/null | head -500'
	fi
}

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
alias catn='/bin/cat'

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


alias vim='nvim'
alias bspwmrc='nvim ~/.config/bspwm/bspwmrc'
alias sxhkdrc='nvim ~/.config/sxhkd/sxhkdrc'
alias zshrc='nvim ~/.zshrc'
alias init.vim='nvim ~/.config/nvim/init.vim'

alias ..='cd ..'
alias py='python'
alias Tex='tllocalmgr'

alias paquetes='pacman -Qe'
alias aur='pacman -Qm'
alias huerfanos='pacman -Qtdq'
