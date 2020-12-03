" Vimrc


"   Plugins
call plug#begin('~/.vim/plugged')
    Plug 'morhetz/gruvbox'
    Plug 'preservim/nerdtree'
    Plug 'christoomey/vim-tmux-navigator'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'dylanaraps/wal.vim'
    Plug 'chxuan/vim-buffer'
    Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
    Plug 'dense-analysis/ale'
    Plug 'zchee/deoplete-jedi'
    Plug 'jiangmiao/auto-pairs'
    Plug 'scrooloose/nerdcommenter'
    Plug 'psf/black', { 'branch': 'stable' }
    Plug 'davidhalter/jedi-vim'
    Plug 'neomake/neomake'
    Plug 'terryma/vim-multiple-cursors'
    Plug 'machakann/vim-highlightedyank'
    Plug 'tmhedberg/SimpylFold'
call plug#end()


" Neobundle
set runtimepath+=~/.vim/bundle/neobundle.vim/
call neobundle#begin(expand('~/.vim/bundle/'))
    NeoBundleFetch 'Shougo/neobundle.vim'
    NeoBundle 'tiagofumo/vim-nerdtree-syntax-highlight'
call neobundle#end()
filetype plugin indent on
NeoBundleCheck


"	Configuración básica

	set nocompatible			"Quitar la compatibilidad con vi
	let mapleader=","			"Fijando tecla líder
	syntax on				"Activando detección de sintaxis
    set mouse=a				"Activando uso del mouse
	set clipboard=unnamedplus		"Activar portapapeles del sistema
	set number				"Numero de lineas
	set relativenumber			"Numero de lineas relativas
	set encoding=utf-8			"Codificacion utf8
	set shiftwidth=4			"Tabulador de 4 esp"acios
	set tabstop=4				"Tab 4
	set expandtab				"Identacion automatica
	set autoindent				"
	filetype indent on
    set ruler
    set showcmd
    set showmatch
    set laststatus=2

    colorscheme wal
    let g:gruvbox_contrast_dark="hard"
    let g:airline#extensions#tabline#enabled = 1
    let g:airline#extensions#tabline#left_alt_sep = '|'
    let g:airline#extensions#tabline#formatter = 'default'
    let g:airline#extensions#tabline#buffer_nr_show = 1
    let g:airline_theme='jellybeans'
    let g:airline_powerline_fonts = 1

    "Atajo de teclas
    nmap <C-m> :NERDTreeToggle<CR>
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
    let NERDTreeQuitOnOpen=1

    "Buffers
    nnoremap <C-PageUp> :bprevious<cr>
    nnoremap <C-PageDown> :bnext<cr>

    "https://github.com/Shougo/deoplete.nvim
    let g:deoplete#enable_at_startup = 1
    autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif
    inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"
    " Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
    let g:UltiSnipsExpandTrigger="<tab>"
    let g:UltiSnipsJumpForwardTrigger="<c-b>"
    let g:UltiSnipsJumpBackwardTrigger="<c-z>"

    " If you want :UltiSnipsEdit to split your window.
    let g:UltiSnipsEditSplit="vertical"

    " disable autocompletion, because we use deoplete for completion
    let g:jedi#completions_enabled = 0

    " open the go-to function in split, not another buffer
    let g:jedi#use_splits_not_buffers = "right"

    " Configurando el Linter de Python
    let g:neomake_python_enabled_makers = ['pylint']
    call neomake#configure#automake('nrwi', 500)

    " Resaltado de copiado
    hi HighlightedyankRegion cterm=reverse gui=reverse
    " 1000 = 1s
    let g:highlightedyank_highlight_duration = 3000
