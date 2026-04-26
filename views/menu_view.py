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

        hint_play_lbl = arcade.Text(
            "ENTER - играть",
            self.window.width / 2,
            self.window.height * 0.55,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
        )

        hint_esc_lbl = arcade.Text(
            "ESC - выйти",
            self.window.width / 2,
            self.window.height * 0.45,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
        )

        self.labels.append(hint_play_lbl)
        self.labels.append(hint_esc_lbl)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """ESC - выход (родительский), ENTER - играть."""
        super().on_key_press(symbol, modifiers)
        if symbol == arcade.key.ENTER:
            self.window.router.show("game")
