#Summary
#This program may load the config file
#then will start the learning sistem

#Imports
from Utilities import Conf, Console, Sort
from Utilities import Convertion_utilities as Convert
from Genetics.Individuals import Individual
from Genetics.Individual_behavior import Neural_behav
import math

#Functions
def get_inputs(inputs_amout: int):
        inputs = []
        for i in range(inputs_amout):
            inputs.append(
            int(
            input('Insert input {}: '.format(i))
            )
            )
        return inputs

def create_generation(size : int, input):
    for i in range(size):
        generation.append(Individual(input))
        brain = Individual.set_brain(neural_struct)

        generation[i].weights = brain[0]
        generation[i].biases = brain[1]



#Variables
generation = []
neural_struct = []

#Main program
Conf.config()

neural_struct = Neural_behav.define_neural(Conf.inputs, Conf.outputs, Conf.layers, Conf.neurons_per_layer)

print(neural_struct)
create_generation(Conf.max_individuals, get_inputs(Conf.inputs))
Console.clear()

for individual in generation:
    print(individual.weights)
    print(individual.biases)
    individual.outputs = individual.think(neural_struct)
    individual.score = individual.set_score([20])
    individual.score = round(individual.score * 10**6)/10**6
    print(individual.score)
    input()

Console.clear()

generation = Sort.by_score(generation)

individual = generation[0] + generation[1]
print(individual.weights)

input()
