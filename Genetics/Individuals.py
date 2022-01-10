import random
from Extentions import Convertion_extentions as Convert
from Genetics.Individual_behavior import Neural_behav

class Individual(object):

    weights = []
    biases = []

    def __init__(self, inputs : int):
        self.score = 0
        self.inputs = inputs


    def __add__(self, i2):
        child = ''
        parent1 = Convert.To_bin(self.x[0])
        parent2 = Convert.To_bin(i2.x[0])
        splitPoint = random.randint(1, len(parent1) - 1)


        for i in range (0, len(parent1), 1):
            if i < splitPoint:
                child += parent1[i]
            else:
                child += parent2[i]

        return Individual(0, [Convert.To_dec(child)])

    @staticmethod
    def set_brain(neural_str):
        weights = [[]]
        biases = [[]]
        for j in range(1, len(neural_str), 1):
            weights.append(Neural_behav.create_weights(neural_str[j], neural_str[j-1]))
            biases.append(Neural_behav.create_biases(neural_str[j]))

        return [weights, biases]

    def train(self):
        for i in range(len(self.inputs)):
            self.inputs[i] *= 3
