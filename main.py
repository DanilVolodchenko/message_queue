from fastapi import FastAPI

from api import router
from game import Server, Game, GameItem, CommandStorage
from container import ioc


def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app


def main() -> None:
    ioc.register('Server', Server)
    ioc.register('Game', Game)
    ioc.register('GameItem', GameItem)
    ioc.register('CommandStorage', CommandStorage)


main()
app = init_app()
