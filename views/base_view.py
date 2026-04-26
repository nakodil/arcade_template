"""Модуль базового представления."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from core.app import App


class BaseView(arcade.View, ABC):
    """Базовое представление."""

    window: App

    @abstractmethod
    def __init__(self) -> None:
        """Инициализирует базовое представление."""
        super().__init__()
        self.sprites = arcade.SpriteList()
        self.labels: list[arcade.Text] = []

    def setup(self) -> None:
        """Исходное состояние."""
        self.sprites.clear()
        self.labels.clear()

    def on_draw(self) -> None:
        """Рисует спрайты и лейблы."""
        self.clear()
        self.sprites.draw()
        for label in self.labels:
            label.draw()

    def on_update(self, delta_time: float) -> None:
        """Обновление."""
        self.sprites.update(delta_time)
