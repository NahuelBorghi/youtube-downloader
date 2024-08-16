# YouTube Music Downloader

Este es un script simple en Python para buscar y descargar música de YouTube en formato mp3.

## Descargas

Puedes descargar las versiones compiladas del programa para diferentes sistemas operativos desde la sección de [Releases](https://github.com/NahuelBorghi/youtube-downloader/releases).

- **Windows**: Descargar el archivo `.exe` y ejecutarlo directamente.
- **Linux**: Descargar el binario correspondiente o el script `.sh`.
- **Código fuente**: También disponible en la misma sección de releases.

## Requisitos para Devs

- Python 3.x
- pip (para instalar las dependencias)

## Instalación de Dependencias

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/NahuelBorghi/youtube-downloader.git
```

2. Instala las dependencias usando pip:

```bash
pip install -r requirements.txt
```

## Uso

1. Navega al directorio del proyecto:

```bash
cd youtube-downloader/
```

2. Ejecuta el script `main.py` dentro de la carpeta `app` y sigue las instrucciones para buscar y descargar música de YouTube.

```bash
cd app
python main.py
```

El script te pedirá ingresar el nombre o frase a buscar en YouTube. Puedes seleccionar un video de la lista de resultados y descargar el audio en formato mp3.

## Inclusión de ffmpeg

Este proyecto incluye `ffmpeg` para la conversión de archivos de audio. `ffmpeg` está licenciado bajo la **Licencia GNU General Public License v3.0 (GPL v3)**. Puedes encontrar los archivos de licencia y la documentación en la carpeta `ffmpeg` incluida en el repositorio.

## Disclaimer

El uso de este software es bajo tu propio riesgo. El autor no se hace responsable del uso que le des a los audios descargados de YouTube. Asegúrate de cumplir con todas las leyes y regulaciones aplicables en tu país antes de utilizar el software para descargar contenido. El contenido descargado debe usarse únicamente para fines personales y no comerciales.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código, realiza un fork del repositorio, haz tus cambios y luego crea una solicitud de extracción.

## Licencia

Este proyecto está licenciado bajo la Licencia GNU General Public License v3.0.
