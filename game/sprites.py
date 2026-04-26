"""Модуль спрайтов."""

from abc import ABC, abstractmethod

import arcade

import config


class GameObject(arcade.Sprite, ABC):
    """Абстрактный игровой объект."""

    @abstractmethod
    def __init__(
            self,
            texture: arcade.Texture,
            scale: float,
            center_x: float,
            center_y: float,
    ) -> None:
        """Инициализация игрового объекта."""
        super().__init__(texture, scale, center_x, center_y)


class Player(GameObject):
    """Игрок с управлением клавишами."""

    def __init__(self, center_x: float, center_y: float) -> None:
        """Инициализация."""
        texture = arcade.load_texture(config.IMG_DIR / "player.png")
        scale = 1.0
        super().__init__(texture, scale, center_x, center_y)
        self.speed = 10

    def move(self, dx: float, dy: float) -> None:
        """Движение."""
        self.center_x += dx * self.speed
        self.center_y += dy * self.speed
