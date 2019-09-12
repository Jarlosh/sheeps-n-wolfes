from typing import Dict

from MapStuff.Creatures.CreatureType import CreatureType
from MapStuff.GameLogic.DecisionFunc import MoveDecision


class StepCollector:
    def __init__(self, game_map,
                 sheep_behaviour,
                 wolf_behaviour):
        self.game_map = game_map

        self.behaviours = {
            CreatureType.SHEEP: sheep_behaviour,
            CreatureType.WOLF: wolf_behaviour
        }




    def collect(self, game_map):
        walkers = dict()
        stayers = dict()
        neutral = dict()

        intelligent_crts, neutral_crts = game_map.get_creatures()
        for loc, crt in intelligent_crts:
            behaviour = self._get_behaviour(crt.crt_type)
            decision = behaviour.decide(game_map, loc, crt)

            decision_type = MoveDecision.classify(decision)
            if decision_type == MoveDecision.Advance:
                target_loc = game_map.get_next_loc(loc, crt.direction)
                walkers[loc] = (crt, target_loc)
            else:
                stayers[loc] = crt
                is_clockwise = decision_type == MoveDecision.TurnClockWise
                crt.rotate(is_clockwise)

        neutral = {loc: crt for loc, crt in neutral_crts}
        return walkers, stayers, neutral



    def _get_behaviour(self, crt_type: CreatureType):
        if crt_type in self.behaviours:
            return self.behaviours[crt_type]
        else:
            raise Exception(f'No behaviour specified for {crt_type.name}')






