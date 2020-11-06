from .base import HttpClient


class Game(HttpClient):
    _game_instance = None

    def create(self):
        resp = self.post("games")
        self._game_instance = resp.json()
        print(self._game_instance)
