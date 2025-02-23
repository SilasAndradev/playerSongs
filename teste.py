import eyed3
from io import BytesIO
from PIL import Image
import requests
import customtkinter as ctk
from tkinter import filedialog

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
        if self.song_path:
            # Aqui você tocaria a música, usando pygame como no exemplo anterior
            print(f"Tocando a música: {self.song_path}")
            self.display_album_cover()
        else:
            print("Nenhuma música selecionada")

    def stop_music(self):
        print("Música parada")
    
    def select_music(self):
        self.song_path = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])
        print(f"Música selecionada: {self.song_path}")
        self.song_image = self.get_album_cover(self.song_path)

    def get_album_cover(self, song_path):
        # Usando eyed3 para acessar os metadados e extrair a capa do álbum
        audio_file = eyed3.load(song_path)
        for tag in audio_file.tag.frame_set:
            if tag.id == 'APIC':  # APIC contém a capa do álbum
                image_data = tag.image_data
                image = Image.open(BytesIO(image_data))
                return image
        return None

    def display_album_cover(self):
        if self.song_image:
            # Exibindo a capa do álbum na interface
            self.song_image = self.song_image.resize((200, 200))  # Redimensionando a imagem
            self.song_cover_photo = ctk.CTkImage(self.song_image)  # Criando a imagem no formato do CTk
            self.album_cover_label.configure(image=self.song_cover_photo)  # Atualizando a imagem no widget
        else:
            print("Nenhuma capa encontrada para essa música.")

# Criação da janela principal
root = ctk.CTk()
music_player = MusicPlayer(root)

# Inicia o loop da interface gráfica
root.mainloop()
