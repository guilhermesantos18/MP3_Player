# Biblioteca GUI
import tkinter as tk
from tkinter import *


# Interface
janela_principal = tk.Tk()
janela_principal.title('Music Here!')
janela_principal.geometry('400x600')

# Menu
menu = tk.Menu(janela_principal)
janela_principal.config(menu=menu)
music_menu = tk.Menu(menu)
menu.add_cascade(label='Opções', menu=music_menu)
music_menu.add_command(label='Pasta Musica')
music_menu.add_command(label='Musica especifíca')

# Icones
icone_stop = tk.PhotoImage(file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_pause_black_24dp.png')
icone_play = tk.PhotoImage(file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_play_arrow_black_24dp.png')
icone_next = tk.PhotoImage(file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_skip_next_black_24dp.png')
icone_previous = tk.PhotoImage(file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_skip_previous_black_24dp.png')

# Criar a Label para icones
stop_music = tk.Label(janela_principal, image=icone_stop)
play_music = tk.Label(janela_principal, image=icone_play)
next_music = tk.Label(janela_principal, image=icone_next)
previous_music = tk.Label(janela_principal, image=icone_previous)

# Para visualizar icones na tela e posicioná-los
stop_music.pack()
play_music.pack()
next_music.pack()
previous_music.pack()

janela_principal.config(menu=menu)
janela_principal.mainloop()
