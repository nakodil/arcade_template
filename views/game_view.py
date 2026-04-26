"""Модуль представления меню."""

import arcade

from .base_view import BaseView


class GameView(BaseView):
    """Представление меню."""

    def __init__(self) -> None:
        """Инициализирует представление меню."""
        super().__init__()
        self.game = self.window.game
        self.setup()
        print(f"[DEBUG:] инит GameViev, игра: {self.game}")

    def setup(self) -> None:
        """Исходное состояние."""
        super().setup()
