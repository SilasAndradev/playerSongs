import eyed3
from io import BytesIO
from PIL import Image
import requests
import customtkinter as ctk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Player de Música")
        self.root.geometry("400x400")

        self.song_path = ""
        self.song_image = None  # Para armazenar a imagem da capa

        # Criação dos widgets
        self.play_button = ctk.CTkButton(self.root, text="Tocar", command=self.play_music)
        self.play_button.pack(pady=20)

        self.stop_button = ctk.CTkButton(self.root, text="Parar", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.select_button = ctk.CTkButton(self.root, text="Selecionar Música", command=self.select_music)
        self.select_button.pack(pady=10)

        self.album_cover_label = ctk.CTkLabel(self.root, text="Capa do Álbum")
        self.album_cover_label.pack(pady=10)

    def play_music(self):
        pygame.init()
        if self.song_path:
            # Aqui você tocaria a música, usando pygame como no exemplo anterior
            print(f"Tocando a música: {self.song_path}")
            self.musica = pygame.mixer.Sound(self.song_path)
            self.musica.play(0)
        else:
            print("Nenhuma música selecionada")

    def stop_music(self):
        self.musica.stop()
    
    def select_music(self):
        self.song_path = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])
        print(f"Música selecionada: {self.song_path}")
       

# Criação da janela principal
root = ctk.CTk()
music_player = MusicPlayer(root)

# Inicia o loop da interface gráfica
root.mainloop()
