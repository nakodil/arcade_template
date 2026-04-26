"""Модуль представления меню."""

import arcade

from game import Player

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
        self._add_player()
        self._add_hints()

    def _add_player(self) -> None:
        """Добавляет игрока в спрайты."""
        player_x = self.window.width / 2
        player_y = self.window.height / 2
        player = Player(player_x, player_y)
        self.sprites.append(player)

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

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """Обработка клавиш."""
        if symbol == arcade.key.ESCAPE:
            self.window.router.show("menu")
