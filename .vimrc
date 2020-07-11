" Vimrc


"   Plugins
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'
Plug 'easymotion/vim-easymotion'
Plug 'preservim/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
call plug#end()


"	Configuración básica

	set nocompatible			"Quitar la compatibilidad con vi
	let mapleader=","			"Fijando tecla líder
	syntax on				"Activando detección de sintaxis
    set mouse=a				"Activando uso del mouse
	set clipboard=unnamedplus		"Activar portapapeles del sistema
	set number				"Numero de lineas
	set relativenumber			"Numero de lineas relativas
	set encoding=utf-8			"Codificacion utf8
	set shiftwidth=4			"Tabulador de 4 espacios
	set tabstop=4				"Tab 4
	set expandtab				"Identacion automatica
	set autoindent				"
	filetype indent on
    set ruler
    set showcmd
    set showmatch
    set laststatus=2
    
    let g:gruvbox_contrast_dark="hard"
    let g:airline#extensions#tabline#enabled = 1
    let g:airline#extensions#tabline#left_alt_sep = '|'
    let g:airline#extensions#tabline#formatter = 'default'
    let g:airline_theme='jellybeans'

"   Atajo de teclas
    nnoremap <F12> :setlocal spell! spelllang=es<Enter>
    nmap <Leader>s <Plug>(easymotion-s2)
    nmap <C-n> :NERDTreeToggle<CR>
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
    let NERDTreeQuitOnOpen=1

