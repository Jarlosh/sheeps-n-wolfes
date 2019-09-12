from random import shuffle, choice

from MapStuff.Creatures.Creature import Grass
from MapStuff.Creatures.Sheep import Sheep
from MapStuff.Creatures.Wolf import Wolf
from MapStuff.Misc.DirectionEnum import Direction


def _make_locations(needed_count, width, height):
    area = width * height
    assert needed_count <= area

    loc_indexes = [i for i in range(area)]
    shuffle(loc_indexes)
    for res_index in range(needed_count):
        index = loc_indexes[res_index]
        yield (index // width, index % width)

def _make_many_crts(crt_class, count, *constructor_args):
    return [crt_class(*constructor_args) for _ in range(count)]


class GameMapGenerator:
    directions = Direction.directions_list()


    @staticmethod
    def _make_crts(crt_args):
        w_count, s_count, g_count = crt_args
        crts = [
            *_make_many_crts(Wolf, w_count),
            *_make_many_crts(Sheep, s_count),
            *_make_many_crts(Grass, g_count)
        ]
        return crts

    @staticmethod
    def make_loc_crt_map(width, height, crt_args, random_directions=True):
        location_map = dict()

        crts = GameMapGenerator._make_crts(crt_args)
        locations_gen = _make_locations(len(crts), width, height)

        for crt in crts:
            if random_directions:
                crt.direction = choice(GameMapGenerator.directions)
            loc = next(locations_gen)
            location_map[loc] = crt
        return location_map


# cra = [80, 10, 10]
# a = GameMapGenerator.make_loc_crt_map(10, 10, cra)
