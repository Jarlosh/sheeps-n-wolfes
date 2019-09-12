from MapStuff.Creatures.CreatureType import CreatureType
from MapStuff.Creatures.Creature import Intelligent


class Wolf(Intelligent):
    crt_type = CreatureType.WOLF
    memory_count = 3
