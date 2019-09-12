from Game import Game
from MapStuff.GameMap import GameMap

_width = 10
_height = 10
WCOUNT = 25
SCOUNT = 25
GCOUNT = 25

crt_args = (WCOUNT, SCOUNT, GCOUNT)
gen_args = (_width, _height)


class Lab:
    def __init__(self):
        pass



    def start(self):
        game_map = GameMap.generate(gen_args, crt_args)
        game = Game(game_map)
        self.play_game(game)


    @staticmethod
    def play_game(game):
        game.resolve_to_end()





lab = Lab()
lab.start()
