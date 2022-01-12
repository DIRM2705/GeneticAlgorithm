#Summary
#This program may load the config file
#then will start the learning sistem

#Imports
from Utilities import Conf, Console, Sort
from Utilities import Convertion_utilities as Convert
from Genetics.Individuals import Individual
from Genetics.Individual_behavior import Neural_behav

#Functions
def welcome():
    Console.clear()
    print('HI, THANK YOU for using DIRM2705\'s genetic algorithm')
    print('Have fun experimenting, if you\'re willing to colaborate you can see source code in https://github.com/DIRM2705/GeneticAlgorithm.git')
    print('')

    Console.wait_for_key()
    Console.clear()


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

def train_and_reproduce():
    global generation
    for individual in generation:
        individual.outputs = individual.think(neural_struct)
        individual.score = individual.set_score(25)
        individual.score = round(individual.score, 6)
        print(individual.score)

        if individual.score > 0.98:
            print('')
            print(individual.weights)
            print(individual.biases)
            print(individual.outputs)
            input()

    generation = Sort.by_score(generation)

    for parents in range(0, Conf.max_parents, 2):
        individual = generation[parents] + generation[parents + 1]
        new_generation.append(individual)

    for i in range(Conf.individuals_to_save):
        if len(new_generation) >= Conf.max_individuals:
            return
        new_generation.append(generation[i])

def complete_generation(input):
    for i in range(len(generation), Conf.max_individuals, 1):
        generation.append(Individual(input))
        brain = Individual.set_brain(neural_struct)

        generation[i].weights = brain[0]
        generation[i].biases = brain[1]

#Variables
generation = []
neural_struct = []
new_generation = []
inputs = []

#Main program
welcome()

#Conf.config()

neural_struct = Neural_behav.define_neural(Conf.inputs, Conf.outputs, Conf.layers, Conf.neurons_per_layer)
print(neural_struct)

inputs = get_inputs(Conf.inputs)

create_generation(Conf.max_individuals, inputs)

Console.clear()
for gen in range(Conf.max_generations):
    train_and_reproduce()
    generation = new_generation
    complete_generation(inputs)

print(generation[0].outputs)
input()


input()
