import random

class Neural_behav(object):

    @staticmethod
    def create_weights(layer1_neuron: int, layer2_neuron: int):
        weights = []
        for i in range(layer1_neuron):
            for i in range(layer2_neuron):
                weight_i = round(random.uniform(0, 1) * 10**6)
                weights.append(weight_i/10**6)
        return weights

    @staticmethod
    def create_biases(neurons_amount : int):
        biases = []
        for i in range(neurons_amount):
            bias_i = round(random.uniform(0, 5) * 10**6)
            biases.append(bias_i/10**6)
        return biases

    @staticmethod
    def define_neural(inputs : int, outputs : int, layers : int, neurons_per_layer : int):
        neural_structure = [inputs, inputs]
        for i in range(layers - 1):
            neural_structure.append(neurons_per_layer)
        neural_structure.append(outputs)
        return neural_structure
