#Summary
#This program may load the config file
#then will start the learning sistem

#Imports
from Extentions import Convertion_extentions as Convert
from Genetics.Individuals import Individual
from Genetics.Individual_behavior import Neural_behav
from Utilities import Conf, Console

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
        generation.append(Individual(inputs))
        brain = Individual.set_brain(neural_struct)

        generation[i].weights = brain[0]
        generation[i].biases = brain[1]


#Variables
max_individuals = 3
inputs = 1
outputs = 1
layers = 2
neurons_per_layer = 3
generation = []
neural_struct = []

#Main program
Conf.config()

neural_struct = Neural_behav.define_neural(inputs, outputs, layers, neurons_per_layer)

print(neural_struct)

create_generation(3, get_inputs(inputs))


for i in generation:
    print(i.weights)
    print(i.biases)
    print('')

input()
Console.clear()
