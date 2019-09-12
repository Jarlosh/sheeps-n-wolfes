from enum import IntEnum


class CreatureType(IntEnum):
    NONE = 0
    SHEEP = 4
    WOLF = 8
    GRASS = 12

    def get_code(self):
        if self.value == 0:
            return 0
        else:
            return 1 / self.value









