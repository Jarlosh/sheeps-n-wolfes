from enum import IntEnum

class Direction(IntEnum):
    North = 0
    East = 1
    South = 2
    West = 3


    @staticmethod
    def rotate(old_direction, is_clockwise):
        delta = 1 if is_clockwise else -1
        return Direction((old_direction.value + delta) % 4)

    @staticmethod
    def directions_list():
        return all_directions


all_directions = [
    Direction.North,
    Direction.East,
    Direction.West,
    Direction.South
    ]
