"""Модуль игровой логики."""

from .sprites import Player


class Logic:
    """Игровая логика."""

    def __init__(self) -> None:
        """Инициализация."""
        self.width = 0
        self.height = 0
        self.active_keys = set()
        self.player: Player | None = None

    def setup(self, window_width: float, window_height: float) -> None:
        """Исходное состояние."""
        self.width = window_width
        self.height = window_height
        player_size = min(self.width, self.height) * 0.2
        self.player = Player(
            player_size,
            player_size,
            self.width / 2,
            self.height / 2,
        )

    def on_update(self, delta_time: float) -> None:
        """Обновление."""
        if self.player:
            self.player.on_keys(self.active_keys)
            self.player.move(delta_time)
            self.player.collide_offscreen(self.width, self.height)

    def on_key_press(self, key_code: int) -> None:
        """Обработка нажатых клавиш."""
        self.active_keys.add(key_code)

    def on_key_release(self, key_code: int) -> None:
        """Обработка отпущенных клавиш."""
        if key_code in self.active_keys:
            self.active_keys.remove(key_code)
