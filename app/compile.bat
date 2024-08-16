@echo off
pyinstaller --noconsole --onefile --add-data "ffmpeg/bin/*;ffmpeg/bin" main.py
pause
