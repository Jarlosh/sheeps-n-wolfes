from typing import Dict, Tuple, Callable, Generator

from MapStuff.Creatures.Creature import Intelligent
from MapStuff.GameLogic.ViewGetter import Point
from MapStuff.Misc.DirectionEnum import Direction

# Point = Tuple[int, int]
# ViewRanges = Dict[Direction, int]



class Behaviour:
    def __init__(self, decide_func, view_func):
        self._decide_func = decide_func
        self._get_view_func = view_func

    def decide(self, game_map, loc: Point, crt: Intelligent):
        view = self._get_view_func(game_map, loc, crt.direction)
        decision_vector = self._decide_func(view, crt)
        decision = decision_vector[0]
        crt.remember(decision)
        return decision
