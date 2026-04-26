"""Модуль спрайтов."""

from abc import ABC, abstractmethod

import arcade

import config
from core import utils


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

    def collide_offscreen(self, max_w: float, max_h: float) -> None:
        """Не дает спрайту выйти за границы окна."""
        self.right = min(self.right, max_w)
        self.left = max(self.left, 0)
        self.top = min(self.top, max_h)
        self.bottom = max(self.bottom, 0)

class Player(GameObject):
    """Игрок с управлением клавишами."""

    def __init__(
            self,
            width: float,
            height: float,
            center_x: float,
            center_y: float,
    ) -> None:
        """Инициализация."""
        texture = arcade.load_texture(config.PLAYER_IMG)
        scale = utils.get_image_scale(texture.width, texture.height, width, height)
        super().__init__(texture, scale, round(center_x), round(center_y))
        self.velocity_vector = arcade.Vec2(0, 0)
        self.speed = 300  # пикселей в секунду
        self.keys = {
            "up": arcade.key.W,
            "down": arcade.key.S,
            "left": arcade.key.A,
            "right": arcade.key.D,
        }

    def move(self, delta_time: float) -> None:
        """Движение."""
        if self.velocity_vector.length() <= 0:
            return
        direction = self.velocity_vector.normalize()
        self.center_x += round(direction.x * self.speed * delta_time)
        self.center_y += round(direction.y * self.speed * delta_time)

    def on_keys(self, keys: set[int]) -> None:
        """Обработка клавиш."""
        d_x, d_y = 0, 0
        if self.keys["up"] in keys:
            d_y += 1
        if self.keys["down"] in keys:
            d_y += -1
        if self.keys["right"] in keys:
            d_x += 1
        if self.keys["left"] in keys:
            d_x += -1
        self.velocity_vector = arcade.Vec2(d_x, d_y)
