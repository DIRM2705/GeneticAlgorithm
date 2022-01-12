import random
import math
import numpy as np
from Utilities import Convertion_utilities as Convert
from Genetics.Individual_behavior import Neural_behav

class Individual(object):

    weights = []
    biases = []
    outputs = []

    def __init__(self, inputs):
        self.score = 0
        self.inputs = inputs


    def __add__(self, i2):
        new_weights = []
        new_biases = []
        for i in range(len(self.weights)):
            neuron_weights = []
            for j in range(len(self.weights[i])):
                neuron_weights.append(Neural_behav.add_binaries(self.weights[i][j], i2.weights[i][j]))
            new_weights.append(neuron_weights)

        for i in range(len(self.biases)):
            neuron_biases = []
            for j in range(len(self.biases[i])):
                neuron_biases.append(Neural_behav.add_binaries(self.biases[i][j], i2.biases[i][j]))
            new_biases.append(neuron_biases)

        new_individual = Individual(self.inputs)
        new_individual.weights = new_weights
        new_individual.biases = new_biases

        return new_individual


    def think(self, neural_str):
        i = 0
        Train_outputs = self.inputs

        for layer in neural_str:
            if i == 0:
                i += 1
                continue
            weight_index = 0
            layer_output = []

            for neuron in range(layer):
                activate = self.biases[i][neuron]
                for ins in range(len(Train_outputs)):

                    activate += self.weights[i][weight_index] * Train_outputs[ins]
                    weight_index += 1

                activate = 1/(1-np.exp(-activate))
                layer_output.append(round(activate, 6))

            Train_outputs = layer_output
            #input()
            i += 1

        return Train_outputs

    def set_score(self, ex_out):
        partial = 0
        for output in self.outputs:
            aux = ex_out - output
            partial = 1 - abs(aux)/100
        return partial

    @staticmethod
    def set_brain(neural_str):
        weights = [[]]
        biases = [[]]
        for j in range(1, len(neural_str), 1):
            weights.append(Neural_behav.create_weights(neural_str[j], neural_str[j-1]))
            biases.append(Neural_behav.create_biases(neural_str[j]))

        return [weights, biases]
