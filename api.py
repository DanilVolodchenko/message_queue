from typing import Annotated, Mapping

from fastapi import APIRouter, Path, Body
from commands import InterpretCommand

router = APIRouter()


@router.post(
    '/game/{game_id}/obj/{game_item_id}/command/{command_id}',
    description='Помещает команду с id=command_id в игру с id=game_id для объекта игры с id=game_item_id'
)
def add_command(
        game_id: Annotated[int, Path(title='id игры')],
        game_item_id: Annotated[int, Path(title='id объекта, которому будет применена команда')],
        command_id: Annotated[int, Path(title='id команды')],
        kwargs: Annotated[Mapping, Body(default_factory=dict, title='id объекта, которому будет применена команда')]
):
    try:
        return InterpretCommand(game_id, game_item_id, command_id, kwargs).execute()
    except Exception as exc:
        return f'({exc.__class__.__name__}) {exc}'
