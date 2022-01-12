import random
from Utilities import Convertion_utilities as Convert

class Neural_behav(object):

    @staticmethod
    def create_weights(layer1_neuron: int, layer2_neuron: int):
        weights = []
        for i in range(layer1_neuron):
            for i in range(layer2_neuron):
                weight_i = round(random.uniform(0, 1), 6)
                weights.append(weight_i)
        return weights

    @staticmethod
    def create_biases(neurons_amount : int):
        biases = []
        for i in range(neurons_amount):
            bias_i = round(random.uniform(0, 5), 6)
            biases.append(bias_i)
        return biases

    @staticmethod
    def define_neural(inputs : int, outputs : int, layers : int, neurons_per_layer : int):
        neural_structure = [inputs, inputs]
        for i in range(layers - 1):
            neural_structure.append(neurons_per_layer)
        neural_structure.append(outputs)
        return neural_structure

    @staticmethod
    def add_binaries(a_bin, b_bin):
        o_bin = ''
        print(a_bin)
        print(b_bin)

        a_bin = int(round(a_bin * 10**6))
        b_bin = int(round(b_bin * 10**6))

        print(a_bin)
        print(b_bin)

        a_bin = Convert.To_bin(a_bin)
        b_bin = Convert.To_bin(b_bin)

        print(a_bin)
        print(b_bin)

        split_point = random.randint(0, len(a_bin) - 1)
        print(split_point)

        for k in range(len(a_bin)):
            if(k < split_point):
                o_bin += a_bin[k]
            else:
                o_bin += b_bin[k]

        print(o_bin)
        o_bin = Convert.To_dec(o_bin)
        o_bin = round(o_bin * 10**-6, 6)
        print(o_bin)
        print('')

        return o_bin
