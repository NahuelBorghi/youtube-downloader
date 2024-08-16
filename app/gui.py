import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar, Button
from downloader import download_audio
from youtubesearchpython import VideosSearch

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Audio Downloader")
        
        self.search_label = tk.Label(root, text="Buscar en YouTube:")
        self.search_label.pack(pady=5)
        
        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.pack(pady=5)
        
        self.search_button = tk.Button(root, text="Buscar", command=self.search_videos)
        self.search_button.pack(pady=5)
        
        self.results_listbox = Listbox(root, width=80, height=15)
        self.results_listbox.pack(pady=5)
        
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.results_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.results_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.download_button = tk.Button(root, text="Descargar", command=self.download_audio)
        self.download_button.pack(pady=5)
        
        self.videos = []
        
    def search_videos(self):
        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Advertencia", "Por favor ingresa un término de búsqueda.")
            return
        
        self.results_listbox.delete(0, tk.END)
        
        result = VideosSearch(query, limit=15)
        self.videos = [(video['title'], video['link']) for video in result.result()['result']]
        
        if not self.videos:
            messagebox.showinfo("Información", "No se encontraron videos.")
            return
        
        for i, (title, _) in enumerate(self.videos, start=1):
            self.results_listbox.insert(tk.END, f"{i}. {title}")
        
    def download_audio(self):
        selection = self.results_listbox.curselection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona un video para descargar.")
            return
        
        index = selection[0]
        title, url = self.videos[index]
        
        # Pedimos el nombre del artista
        artist = simpledialog.askstring("Artista", "Ingresa el nombre del artista:")
        if not artist:
            artist = "Desconocido"
        
        download_audio(title, url, artist)
