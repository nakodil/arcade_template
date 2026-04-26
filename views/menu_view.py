"""Модуль представления меню."""

import arcade

from .base_view import BaseView


class MenuView(BaseView):
    """Представление меню."""

    def __init__(self) -> None:
        """Инициализирует представление меню."""
        super().__init__()
        self.setup()

    def setup(self) -> None:
        """Исходное состояние."""
        super().setup()
        self._add_hints()

    def _add_hints(self) -> None:
        """Добавляет лейбл подсказки."""
        hints_lbl = arcade.Text(
            "ENTER - играть, ESC - выйти",
            self.window.width / 2,
            self.window.height * 0.55,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
        )
        self.labels.append(hints_lbl)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """ESC - выход, ENTER - играть."""
        if symbol == arcade.key.ESCAPE:
            self.window.router.exit()
        if symbol == arcade.key.ENTER:
            self.window.router.show("game")
