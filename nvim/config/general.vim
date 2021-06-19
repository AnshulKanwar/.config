syntax enable
set number
set termguicolors
filetype plugin on

let g:python3_host_prog = "/usr/bin/python"

let g:tokyonight_style = 'night' " available: night, storm
let g:tokyonight_enable_italic = 1
let g:tokyonight_italic_comments = 1
let g:tokyonight_italic_keywords = 1
let g:tokyonight_italic_functions = 1
let g:tokyonight_italic_variables = 1
let g:tokyonight_hide_inactive_statusline = 1
let g:tokyonight_dark_float = 1
let g:tokyonight_transparent_background = 1

colorscheme tokyonight

set nowrap
" set clipboard+=unnamedplus
let g:rainbow_active = 1
let g:NERDCreateDefaultMappings = 1

set tabstop=8 softtabstop=4 expandtab shiftwidth=4 smarttab
autocmd FileType rust set softtabstop=4 expandtab

set laststatus=0
let s:hidden_all = 0
function! ToggleHiddenAll()
    if s:hidden_all  == 0
        let s:hidden_all = 1
        set noshowmode
        set noruler
        set laststatus=0
        set noshowcmd
    else
        let s:hidden_all = 0
        set showmode
        set ruler
        set laststatus=2
        set showcmd
    endif
endfunction

nnoremap <S-h> :call ToggleHiddenAll()<CR>

set hidden
set cmdheight=2
set updatetime=300
set signcolumn=yes

if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

let g:rainbow_guifgs = ['#bb9af7', '#ff768e', '#9ece6a', '#7aa2f7', '#ff9e64']

command! -nargs=0 Prettier :CocCommand prettier.formatFile
