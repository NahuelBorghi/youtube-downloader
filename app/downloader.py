import os
import yt_dlp
from tkinter import messagebox

def download_audio(title, url, artist):
    try:
        # Creamos el directorio del artista si no existe
        output_dir = os.path.join(os.getcwd(), "descargas", artist)
        os.makedirs(output_dir, exist_ok=True)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'ffmpeg_location': os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin')
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        messagebox.showinfo("Éxito", f"Descarga completada en: {output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error durante la descarga: {str(e)}")
