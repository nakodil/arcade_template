"""Модуль конфигурации."""

import sys
from pathlib import Path

# Определение корневой папки
if getattr(sys, "frozen", False):  # запуск из EXE (Pyinstaller ставит frozen)
    BASE_DIR = Path(getattr(sys, "_MEIPASS", sys.executable)).resolve()
else:  # запуск из консоли
    BASE_DIR = Path(__file__).resolve().parent

# Остальные пути через корневую папку
ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "img"
SOUND_DIR = ASSETS_DIR / "sound"

# Текстуры спрайтов
PLAYER_IMG = IMG_DIR / "player.png"

# Заголовок окна
TITLE = "Мое приложение на Python Arcade"
