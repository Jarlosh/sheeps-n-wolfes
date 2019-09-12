from MapStuff.Creatures.CreatureType import CreatureType
from MapStuff.Misc.DirectionEnum import Direction

MEMORY_DEFAULT_VAL = 0

class Creature:
    crt_type = CreatureType.NONE
    is_intelligent = False

    def get_crt_code(self):
        assert self.crt_type != CreatureType.NONE
        return 1 / self.crt_type.value

    def __str__(self):
        return self.crt_type.name

class Intelligent(Creature):
    max_hp = 1
    memory_count = 0
    is_intelligent = True

    def __init__(self):
        self.hp = self.max_hp
        self.direction = Direction.North
        self._memory = [MEMORY_DEFAULT_VAL] * self.memory_count

    def rotate(self, is_clockwise):
        self.direction = Direction.rotate(self.direction, is_clockwise)

    def remember(self, item):
        self._memory.pop()
        self._memory.insert(0, item)

    def get_memory(self):
        return self._memory.copy()

    def get_crt_code(self):
        assert self.crt_type != CreatureType.NONE
        return 1 / (self.crt_type.value + self.direction.value)


class Grass(Creature):
    crt_type = CreatureType.GRASS



