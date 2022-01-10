#Summary
#This program may load the config file
#then will start the learning sistem

#Imports
from Utilities import Conf, Console
from Extentions import Convertion_extentions as Convert
from Genetics.Individuals import Individual
from Genetics.Individual_behavior import Neural_behav

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

def create_generation(size1000 : int, input):
    for i in range(size):
        generation.append(Individual(Conf.inputs))
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

create_generation(3, get_inputs(Conf.inputs))


for i in generation:
    print(i.weights)
    print(i.biases)
    print('')

input()
Console.clear()

print(Convert.To_bin(4))
