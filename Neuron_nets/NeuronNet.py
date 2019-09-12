import math
from typing import Sequence


def sigmoid(x):
    return 1 / (1 + math.e**(-x))

def evaluate(vector, weights, count):
    return sigmoid(sum((vector[i] * weights[i] for i in range(count))))

def lazy_evaluate(vector, weight_iter):
    return sigmoid(sum((v * w for v, w in zip(iter(vector), weight_iter))))

class NeuronNet:
    @staticmethod
    def make_net_func(in_count: int, transit_layers: Sequence[int]):
        tr_count = len(transit_layers)
        layers = transit_layers

        def neuron_net(vector, weights):
            w_iter = iter(weights)
            prev_count = in_count
            for i in range(tr_count):
                nv = []
                for j in range(layers[i]):
                    nv.append(lazy_evaluate(vector, (next(w_iter) for _ in range(prev_count))))
                vector = nv
                prev_count = layers[i]
            return vector
        return neuron_net

    @staticmethod
    def make_wrapped_net_func(in_count: int, transit_layers: Sequence[int], weights):
        net = NeuronNet.make_net_func(in_count, transit_layers)
        def neuron_net(vector):
            return net(vector, weights)
        return neuron_net
