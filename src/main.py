
import customtkinter as ctk
import os
from pathlib import Path
from PIL import Image, ImageTk
from ScrollBarFrame import ScrollBarMainFrame
from MusicPlayer import MusicPlayer

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Player de Música")
        self.geometry("400x500")
        self.start_app()

    def start_app(self):
        self.main_frame = ctk.CTkFrame(self, height=500, width=400)
        self.main_frame.grid(row=0,column=0, padx=0, pady=0, sticky="nsew")

        self.ScrollBarMain_frame_list_songs = ScrollBarMainFrame(master=self, width=380, height=500)
        self.ScrollBarMain_frame_list_songs.grid(row=0,column=0, padx=0, pady=0, sticky="nsew")

        self.musicas = self.ScrollBarMain_frame_list_songs.select_songs(self.ScrollBarMain_frame_list_songs)


if __name__=='__main__':
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()