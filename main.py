# Biblioteca GUI
import tkinter as tk
# Escolher a pasta das musicas
from tkinter import filedialog
# Reproduzir a música
from pygame import mixer

mixer.init()
import os

lista_musicas = []


def tocar_musica():
    mixer.music.load(lista_musicas[0])
    mixer.music.play()


def escolher_pasta_musica():
    music_dir = filedialog.askdirectory()
    for music in os.listdir(music_dir):
        lista_musicas.append(music_dir + '/' + music)
    print(lista_musicas)


# Interface
janela_principal = tk.Tk()
janela_principal.title('Music Here!')
janela_principal.geometry('400x600')

# Menu
menu = tk.Menu(janela_principal)
janela_principal.config(menu=menu)
# tearoff remover linha a tracejado
music_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Opções', menu=music_menu)
music_menu.add_command(label='Pasta Musica', command=escolher_pasta_musica)
music_menu.add_command(label='Musica especifíca')

# Icones
icone_stop = tk.PhotoImage(
    file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_pause_black_24dp.png')
icone_play = tk.PhotoImage(
    file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_play_arrow_black_24dp.png')
icone_next = tk.PhotoImage(
    file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_skip_next_black_24dp.png')
icone_previous = tk.PhotoImage(
    file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\projetospython\MP3_Player\Icons\outline_skip_previous_black_24dp.png')

# Criar a Label para icones
stop_music = tk.Button(janela_principal, image=icone_stop, borderwidth=0)
play_music = tk.Button(janela_principal, image=icone_play, borderwidth=0, command=tocar_musica)
next_music = tk.Button(janela_principal, image=icone_next, borderwidth=0)
previous_music = tk.Button(janela_principal, image=icone_previous, borderwidth=0)

# Para visualizar icones na tela e posicioná-los
stop_music.pack()
play_music.pack()
next_music.pack()
previous_music.pack()

janela_principal.mainloop()
