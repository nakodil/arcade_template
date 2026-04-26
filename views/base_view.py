"""Модуль базового представления."""

import arcade


class BaseView(arcade.View):
    """Базовое представление."""

    def __init__(self) -> None:
        """Инициализирует базовое представление."""
        super().__init__()
        self.sprites = arcade.SpriteList()
        self.labels: list[arcade.Text] = []

    def setup(self) -> None:
        """Исходное состояние."""
        self.sprites.clear()
        self.labels.clear()

    def on_draw(self) -> bool | None:
        """Рисует спрайты и лейблы."""
        self.clear()
        self.sprites.draw()
        for label in self.labels:
            label.draw()

    def on_update(self, delta_time: float) -> bool | None:
        """Обновление."""

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """Обработка нажатий клавиш."""
        if symbol == arcade.key.ESCAPE:
            arcade.exit()
