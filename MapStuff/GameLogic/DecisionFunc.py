from collections import Callable
from enum import Enum

from MapStuff.Creatures.Creature import Intelligent
from Neuron_nets.NeuronNet import NeuronNet


class MoveDecision(Enum):
    TurnCounterClockWise = -1
    Advance = 0
    TurnClockWise = 1

    @staticmethod
    def classify(net_output_number):
        if net_output_number < 1/3:
            return MoveDecision.TurnCounterClockWise
        elif net_output_number < 2/3:
            return MoveDecision.Advance
        else:
            return MoveDecision.TurnClockWise

class DecisionFunc(Callable):
    def __init__(self, in_count, layers, weights):
        self._my_decision_func = self._make_decision_func(in_count, layers, weights)

    @staticmethod
    def _make_decision_func(in_count, layers, weights):
        return NeuronNet.make_wrapped_net_func(in_count, layers, weights)

    @staticmethod
    def _make_net_input(view_vector, crt: Intelligent):
        input_vector = view_vector + crt.get_memory()
        return input_vector


    def __call__(self, view, crt: Intelligent) -> MoveDecision:
        net_input = self._make_net_input(list(view), crt)
        res = self._my_decision_func(net_input)
        return res

