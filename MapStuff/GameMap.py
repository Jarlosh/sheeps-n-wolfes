import itertools
from random import sample, shuffle
from typing import Sequence, Tuple

from MapStuff.Creatures.Creature import Creature
from MapStuff.GameLogic.StepCollector import StepCollector
from MapStuff.MapGenerator import GameMapGenerator
from MapStuff.Misc.Alliases import Point
from MapStuff.Misc.DirectionEnum import Direction

directed_offset = {
    Direction.North: (0, 1),
    Direction.East: (1, 0),
    Direction.South: (0, -1),
    Direction.West: (-1, 0)
}

class GameMap:
    def __init__(self, w, h, crt_loc_map):
        self.width = w
        self.height = h
        self._crt_by_loc_map = crt_loc_map

    @staticmethod
    def make_from_args(width, height, crt_args):
        crt_loc_map = GameMapGenerator.make_loc_crt_map(width, height, crt_args)
        return GameMap(width, height, crt_loc_map)

    def clamp_point(self, point: Point):
        return point[0] % self.width, \
               point[1] % self.height

    def get_next_loc(self, start_loc: Point, step_direction: Direction) -> Point:
        offset = directed_offset[step_direction]
        new_loc = (start_loc[0] + offset[0],
                   start_loc[1] + offset[1])
        return self.clamp_point(new_loc)


    def get_creatures(self):
        intelligent = []
        neutral = []
        for loc, crt in self._crt_by_loc_map.items():
            if crt.is_intelligent:
                intelligent.append((loc, crt))
            else:
                neutral.append((loc, crt))
        return intelligent, neutral

    def get_crt_at(self, loc: Point):
        loc = self.clamp_point(loc)
        if loc in self._crt_by_loc_map:
            return self._crt_by_loc_map[loc]
        else:
            return None

    def get_crt_code_at(self, loc: Point):
        crt = self.get_crt_at(loc)
        if crt:
            return crt.crt_type.get_code()
        else:
            return 0

    def collect_step(self, collector: StepCollector):
        return collector.collect(self)
