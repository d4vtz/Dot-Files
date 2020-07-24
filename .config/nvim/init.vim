" Vimrc


"   Plugins
call plug#begin('~/.vim/plugged')
    Plug 'morhetz/gruvbox'
    Plug 'easymotion/vim-easymotion'
    Plug 'preservim/nerdtree'
    Plug 'christoomey/vim-tmux-navigator'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'dylanaraps/wal.vim'
    Plug 'junegunn/fzf'
    Plug 'pbogut/fzf-mru.vim'
    Plug 'chxuan/vimplus-startify'
    Plug 'chxuan/vim-buffer'
    Plug 'ryanoasis/vim-devicons'
    Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
    Plug 'dense-analysis/ale'
call plug#end()


" Neobundle
set runtimepath+=~/.vim/bundle/neobundle.vim/
call neobundle#begin(expand('~/.vim/bundle/'))
    NeoBundleFetch 'Shougo/neobundle.vim'
    NeoBundle 'tiagofumo/vim-nerdtree-syntax-highlight'
    NeoBundle 'SirVer/ultisnips'
    NeoBundle 'honza/vim-snippets'
    NeoBundle 'lervag/vimtex'
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
	set shiftwidth=4			"Tabulador de 4 espacios
	set tabstop=4				"Tab 4
	set expandtab				"Identacion automatica
	set autoindent				"
	filetype indent on
    set ruler
    set showcmd
    set showmatch
    set laststatus=2
    
    colorscheme wal
    "let g:gruvbox_contrast_dark="hard"
    let g:airline#extensions#tabline#enabled = 1
    let g:airline#extensions#tabline#left_alt_sep = '|'
    let g:airline#extensions#tabline#formatter = 'default'
    let g:airline#extensions#tabline#buffer_nr_show = 1
    let g:airline_theme='jellybeans'
    let g:airline_powerline_fonts = 1

    "Atajo de teclas
    nnoremap <F12> :setlocal spell! spelllang=es<Enter>
    nmap <Leader>s <Plug>(easymotion-s2)
    nmap <C-n> :NERDTreeToggle<CR>
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
    let NERDTreeQuitOnOpen=1

    "Buffers
    nnoremap <C-PageUp> :bprevious<cr>
    nnoremap <C-PageDown> :bnext<cr>

    "https://github.com/Shougo/deoplete.nvim
    let g:deoplete#enable_at_startup = 1

    " Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
    let g:UltiSnipsExpandTrigger="<tab>"
    let g:UltiSnipsJumpForwardTrigger="<c-b>"
    let g:UltiSnipsJumpBackwardTrigger="<c-z>"

    " If you want :UltiSnipsEdit to split your window.
    let g:UltiSnipsEditSplit="vertical"

" This is new style
call deoplete#custom#var('omni', 'input_patterns', {
      \ 'tex': g:vimtex#re#deoplete
      \})
" settings for sumatraPDF
let g:vimtex_view_general_viewer = 'zathura'
let g:vimtex_view_general_options
    \ = '-reuse-instance -forward-search @tex @line @pdf'
let g:vimtex_view_general_options_latexmk = '-reuse-instance'
let g:vimtex_compiler_progname = 'nvr'
