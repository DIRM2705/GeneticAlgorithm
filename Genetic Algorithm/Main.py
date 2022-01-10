#Summary
#This program may load the config file
#then will start the learning sistem

#Imports
from Utilities import Conf, Console
from Utilities import Convertion_extentions as Convert
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
create_generation(3, get_inputs(Conf.inputs))

for individual in generation:
    print(individual.weights)
    print(individual.biases)
    individual.outputs = individual.train(neural_struct)
    individual.score = individual.set_score([20])
    print(individual.score)
    input()

Console.clear()

print(Convert.To_bin(4))

print(Convert.To_dec('00000100'))
