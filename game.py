from typing import Type
from queue import Queue

from interfaces import ICommand


class GameItem:
    """Игровой объект."""
    queue: Queue = Queue()


class Game:
    """Объект игры со всем игровыми объектами."""

    game_items: dict[int, GameItem] = {}

    @classmethod
    def get_item_by_id(cls, ident: int) -> GameItem:
        try:
            return cls.game_items[ident]
        except KeyError:
            raise KeyError(f'Игровой объект с id={ident} не найден')

    @classmethod
    def register(cls, obj_id: int, obj: GameItem):
        cls.game_items[obj_id] = obj


class Server:
    """Объект со всем играми."""

    games: dict[int, Game] = {}

    @classmethod
    def get_game_by_id(cls, ident: int) -> Game:
        try:
            return cls.games[ident]
        except KeyError:
            raise KeyError(f'Игра с id={ident} не найдена')

    @classmethod
    def register(cls, game_id: int, game: Game) -> None:
        cls.games[game_id] = game


class CommandStorage:
    """Объект со всем играми."""

    commands: dict[int, Type[ICommand]] = {}

    @classmethod
    def get_command_by_id(cls, ident: int) -> Type[ICommand]:
        try:
            return cls.commands[ident]
        except KeyError:
            raise KeyError(f'Команда с id={ident} не найдена')

    @classmethod
    def register(cls, command_id: int, command: Type[ICommand]) -> None:
        cls.commands[command_id] = command
