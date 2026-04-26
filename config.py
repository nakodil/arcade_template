"""Модуль конфигурации."""

import sys
from pathlib import Path

if getattr(sys, "frozen", False):  # запуск из EXE (Pyinstaller ставит frozen)
    BASE_DIR = Path(getattr(sys, "_MEIPASS", sys.executable)).resolve()
else:  # запуск из консоли
    BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "images"
SOUND_DIR = ASSETS_DIR / "sound"

TITLE = "Мое приложение на Python Arcade"
