import pytest
from fastapi.testclient import TestClient
from interfaces import ICommand
from main import app
from container import ioc


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

class TestCommand(ICommand):
    def execute(self) -> None:
        ...

def test_endpoint_if_game_does_not_exists(client: TestClient) -> None:
    response = client.post('/game/1/obj/2/command/3', json={})

    assert response.status_code == 200
    assert response.json() == "(KeyError) 'Игра с id=1 не найдена'"


def test_endpoint_if_game_item_does_not_exists(client: TestClient) -> None:
    game = ioc.resolve('Game')
    server = ioc.resolve('Server')

    server.register(1, game)

    response = client.post('/game/1/obj/2/command/3', json={})

    assert response.status_code == 200
    assert response.json() == "(KeyError) 'Игровой объект с id=2 не найден'"


def test_endpoint_if_command_does_not_exists(client: TestClient) -> None:
    game_item = ioc.resolve('GameItem')
    game = ioc.resolve('Game')
    server = ioc.resolve('Server')

    server.register(1, game)
    game.register(2, game_item)

    response = client.post('/game/1/obj/2/command/3', json={})

    assert response.status_code == 200
    assert response.json() == "(KeyError) 'Команда с id=3 не найдена'"


def test_queue_if_not_invoke_endpoint() -> None:
    game_item = ioc.resolve('GameItem')
    game = ioc.resolve('Game')
    server = ioc.resolve('Server')
    command_storage = ioc.resolve('CommandStorage')

    server.register(1, game)
    game.register(2, game_item)
    command_storage.register(3, TestCommand)

    assert game_item.queue.empty() == True

def test_endpoint_in_correct_context(client: TestClient) -> None:
    game_item = ioc.resolve('GameItem')
    game = ioc.resolve('Game')
    server = ioc.resolve('Server')
    command_storage = ioc.resolve('CommandStorage')

    server.register(1, game)
    game.register(2, game_item)
    command_storage.register(3, TestCommand)

    response = client.post('/game/1/obj/2/command/3', json={})

    assert response.status_code == 200
    assert game_item.queue.empty() == False
