from interfaces import ICommand
from game import Server, CommandStorage
from container import ioc


class InterpretCommand(ICommand):
    def __init__(self, game_id: int, game_item_id: int, command_id: int, kwargs) -> None:
        self.game_id = game_id
        self.game_item_id = game_item_id
        self.command_id = command_id
        self.kwargs = kwargs

    def execute(self) -> None:
        server: Server = ioc.resolve('Server')
        game_item = server.get_game_by_id(self.game_id).get_item_by_id(self.game_item_id)
        storage: CommandStorage = ioc.resolve('CommandStorage')
        command = storage.get_command_by_id(self.command_id)
        game_item.queue.put(command(**self.kwargs))
