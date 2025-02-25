import customtkinter as ctk
import os
from pathlib import Path
from MusicPlayer import MusicPlayer

class ScrollBarMainFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
    
    def select_songs(self, frame):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.SONGS_DIR = os.path.join(self.BASE_DIR, "assets", "songs")   
        musicas = []
        self.button_list = []
        for arquivo in Path(self.SONGS_DIR).iterdir():
            if arquivo.suffix in [".mp3", ".wav"]: 
                musicas.append((arquivo.name.replace('.mp3', ''), arquivo))

        for lista_info in musicas:
            button = ctk.CTkButton(frame, text=lista_info[0], width=100, height=24)
            if self.command is not None:
                button.configure(command=lambda: self.command())
            button.grid(row=len(self.button_list), column=0, pady=(0, 10), padx=5)
            if button.is_clicked():
                pass
            self.button_list.append(button)
        