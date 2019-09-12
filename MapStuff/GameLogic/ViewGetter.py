from collections import Callable
from typing import Tuple, Dict, Sequence

# from MapStuff.GameMap import GameMap
from MapStuff import GameMap
from MapStuff.Misc.DirectionEnum import Direction

Point = Tuple[int, int]
ViewRanges = Dict[Direction, int]

class ViewGetter(Callable):
    def __init__(self, view_ranges: ViewRanges):
        self.view_ranges = view_ranges
        self.view_height = view_ranges[Direction.North] + 1 + view_ranges[Direction.South]
        self.view_width = view_ranges[Direction.West] + 1 + view_ranges[Direction.East]
        self._my_view_getter = self._make_view_getter(view_ranges)

    @staticmethod
    def _make_view_getter(view_ranges: ViewRanges):
        north_range = view_ranges[Direction.North]
        west_range = view_ranges[Direction.West]
        south_range = view_ranges[Direction.South]
        east_range = view_ranges[Direction.East]

        def northern_yield(loc):
            x, y = loc
            for nx in range(x - west_range, x + east_range + 1):
                for ny in range(y - north_range, y + south_range + 1):
                    yield nx, ny

        def eastern_yield(loc):
            x, y = loc
            for ny in range(y - north_range, y + south_range + 1):
                for nx in range(x - west_range, x + east_range + 1)[::-1]:
                    yield nx, ny

        def yield_view(loc: Point, direction: Direction):
            seen_locations = None
            if direction == Direction.North:
                seen_locations = northern_yield(loc)
            elif direction == Direction.South:
                seen_locations = list(northern_yield(loc))[::-1]

            elif direction == Direction.East:
                seen_locations = eastern_yield(loc)
            elif direction == Direction.West:
                seen_locations = list(eastern_yield(loc))[::-1]

            for seen_location in seen_locations:
                yield seen_location

        def get_view(game_map: GameMap, loc: Point, direction: Direction):
            for seen_loc in yield_view(loc, direction):
                yield game_map.get_crt_code_at(seen_loc)

        return get_view



    def __call__(self, game_map: GameMap, loc: Point, direction: Direction) -> Sequence[int]:
        for seen_loc in self._my_view_getter(game_map, loc, direction):
            yield seen_loc
