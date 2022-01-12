import random
import math
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
            neuron_biases = []
            for j in range(len(self.weights[i])):
                neuron_weights.append(Neural_behav.add_binaries(self.weights[i][j], i2.weights[i][j]))
            new_weights.append(neuron_weights)

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
            print('Layer No. {}'.format(i + 1))
            weight_index = 0
            layer_output = []

            for neuron in range(layer):
                print('Neuron No. {}'.format(neuron + 1))
                print('Bias = {}'.format(self.biases[i][neuron]))
                neuron_output = []
                for ins in range(len(Train_outputs)):
                    print('Input No. ' + str(ins + 1))
                    print('Weight No. ' + str(weight_index))
                    print(self.weights[i][weight_index])

                    neuron_output.append(
                    self.weights[i][weight_index] * Train_outputs[ins] + self.biases[i][neuron]
                    )

                    weight_index += 1

                layer_output.append(sum(neuron_output))

            print(layer_output)
            Train_outputs = layer_output
            i += 1
        return Train_outputs

    def set_score(self, ex_out):
        partial = 0
        for i in range(len(self.outputs)):
            partial += ex_out[i] - self.outputs[i]
        return partial

    @staticmethod
    def set_brain(neural_str):
        weights = [[]]
        biases = [[]]
        for j in range(1, len(neural_str), 1):
            weights.append(Neural_behav.create_weights(neural_str[j], neural_str[j-1]))
            biases.append(Neural_behav.create_biases(neural_str[j]))

        return [weights, biases]
