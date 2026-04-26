"""Модуль приложения."""

import arcade

import config
from game import Logic
from views import GameView, MenuView

from .sound import SoundManager


class App(arcade.Window):
    """Приложение: фасад систем управления к представлениям (arcade.View)."""

    def __init__(self) -> None:
        """Инициализирует приложение.

        Системы:
            менеджер звуков: загрузка, проигрывание, остановка
            представление: спрайты, текстовые объекты, орисовка
            роутер: переключение представлений
        """
        super().__init__(fullscreen=True, title=config.TITLE)
        self.sound = SoundManager()
        self.sound.load_sounds(config.SOUND_DIR)
        self.router = ViewsManager(self)
        self.game = Logic()
        self.setup()

    def setup(self) -> None:
        """Возврат в исходное состояние."""
        self.sound.setup()
        self.router.setup()
        self.router.show("menu")

    def on_update(self, delta_time: float) -> bool | None:
        """Обновление."""
        self.sound.on_update()
        self.router.on_update()
        self.game.on_update()


class ViewsManager:
    """Роутер: переключает представления окна."""

    def __init__(self, window: arcade.Window) -> None:
        """Инициализирует роутер."""
        self.window = window
        self.routs = {
            "menu": MenuView,
            "game": GameView,
        }

    def setup(self) -> None:
        """Исходное состояние."""

    def on_update(self) -> None:
        """Обновление."""

    def show(self, view_name: str) -> None:
        """Показывает представление в окне."""
        view = self.routs[view_name]()
        self.window.show_view(view)

    def exit(self) -> None:
        """Завершает приложение."""
        arcade.exit()
