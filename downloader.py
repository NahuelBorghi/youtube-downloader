from youtubesearchpython import VideosSearch
from pytube import YouTube
import os

def buscar_videos(query):
    result = VideosSearch(query, limit = 15)
    videos = [(video['title'], video['link']) for video in result.result()['result']]
    return videos

def mostrar_opciones(videos):
    for i, (titulo, _) in enumerate(videos, start=1):
        print(f"{i}. {titulo}")

def descargar_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        if audio:
            # Descargar el audio con extensión mp4
            audio.download(output_path='.', filename='audio_temp.mp4')
            # Renombrar el archivo descargado a formato mp3
            os.rename('audio_temp.mp4', f'{yt.author + ' - ' + yt.title}.mp3')
            print(f"Descarga del audio '{yt.title}' completada.")
        else:
            print("No se pudo descargar el audio del video.")
    except Exception as e:
        print(f"Ocurrió un error durante la descarga del audio: {str(e)}")

def main():
    while True:
        busqueda = input("Ingresa el nombre o frase a buscar en YouTube (o escribe 'salir' para terminar): ")
        os.system('cls')
        if busqueda.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        videos_encontrados = buscar_videos(busqueda)
        
        if not videos_encontrados:
            print("No se encontraron videos para la búsqueda proporcionada.")
            continue
        
        print("Videos encontrados:")
        mostrar_opciones(videos_encontrados)
        
        opcion = input("Selecciona el número del video que quieres descargar (1-15) o escribe 'volver' para realizar otra búsqueda: ")
        if opcion.lower() == 'volver':
            continue
        
        try:
            opcion = int(opcion)
            if 1 <= opcion <= 15:
                _, url_video = videos_encontrados[opcion - 1]
                print("Descargando audio...")
                descargar_audio(url_video)
                print("¡Descarga completada!")
            else:
                print("Opción inválida. Debes seleccionar un número del 1 al 15.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()