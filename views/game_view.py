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

    def setup(self) -> None:
        """Исходное состояние."""
        super().setup()
        self.game.setup(self.window.width, self.window.height)
        if self.game.player:
            self.sprites.append(self.game.player)
        self._add_hints()

    def _add_hints(self) -> None:
        """Добавляет лейбл подсказки."""
        hints_lbl = arcade.Text(
            "WSAD - двигаться, ESC - выйти",
            self.window.width / 2,
            self.window.height * 0.1,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
        )
        self.labels.append(hints_lbl)

    def on_key_press(self, key_code: int, modifiers: int) -> None:
        """Обработка нажатых клавиш."""
        if key_code == arcade.key.ESCAPE:
            self.window.router.show("menu")
        self.game.on_key_press(key_code)

    def on_key_release(self, key_code: int, modifiers: int) -> None:
        """Обработка отпущенных клавиш."""
        self.game.on_key_release(key_code)
