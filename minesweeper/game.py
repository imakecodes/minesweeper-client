from http import HTTPStatus

from .base import HttpClient
from . import exceptions


class Game(HttpClient):
    _game_instance = None

    def create(self):
        resp = self.post("games")
        self._game_instance = resp.json()

    def get_one(self, game_id):
        resp = self.get(f"games/{game_id}")
        if resp.status_code == HTTPStatus.NOT_FOUND:
            raise exceptions.GameNotfound(f"Game {game_id} does not exist")
        self._game_instance = resp.json()
