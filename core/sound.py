"""Модуль управления звуком."""

from __future__ import annotations

from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from pathlib import Path

    import pyglet.media


class SoundManager:
    """Проигрыватель звуков."""

    def __init__(self) -> None:
        """Инициализирует менеджер, загружает звуки."""
        self.is_mute: bool = False

        self.sounds_map: dict[str, str] = {}
        self.active_players: list[pyglet.media.Player] = []

    def load_sounds(self, path: Path) -> None:
        """Загружает звуки из всех файлов папки path."""
        valid_extensions = {".wav", ".mp3", ".ogg", ".m4a"}
        self.sounds = {
            file.stem: arcade.load_sound(file)
            for file in path.iterdir()
            if file.is_file() and file.suffix.lower() in valid_extensions
        }

    def setup(self) -> None:
        """Исходное состояние."""
        self.stop_all()

    def on_update(self) -> None:
        """Удаляет плееры, которые завершили воспроизведение."""
        self.active_players = [
            player for player in self.active_players
            if player.playing
        ]

    def play(
            self,
            sound_name: str,
            volume: float = 0.5,
            *,
            is_loop: bool = False,
    ) -> None:
        """Проигрывает звук один раз или циклично.

        Args:
            sound_name: Ключ звука из словаря self.sounds
            volume: Громкость 0.0-1.0
            is_loop: сыграть 1 раз или повторять

        """
        if self.is_mute:
            return

        sound: arcade.Sound | None = self.sounds.get(sound_name)
        if not sound:
            return

        player: pyglet.media.Player | None = arcade.play_sound(
            sound,
            loop=is_loop,
            volume=volume,
        )
        if player:
            self.active_players.append(player)

    def stop_all(self) -> None:
        """Останавливает все активные плееры."""
        for player in self.active_players:
            arcade.stop_sound(player)
        self.active_players.clear()

    def toggle_mute(self) -> bool:
        """Переключает состояние звука и возвращает текущее состояние."""
        self.is_mute = not self.is_mute
        if self.is_mute:
            self.stop_all()
        return self.is_mute
