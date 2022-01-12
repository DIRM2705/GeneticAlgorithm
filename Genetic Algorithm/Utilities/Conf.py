from Utilities import Console

inputs = 1
outputs = 1
layers = 4
neurons_per_layer = 9
max_bits = 28
max_individuals = 1000
max_parents = 10
children_per_couple = 5
mutation_rate = 25
max_generations = 500000
individuals_to_save = 200


def config():
    try:
        with open('GenAlg.conf', 'r') as f:
            value = []
            lines = f.readlines()
            for line in lines:
                if line == '\n':
                    continue
                else:
                    value.append(int(line.split('=')[1]))

            if inputs != value[0]:
                raise ValueError('Inputs mismatch')
            if outputs != value[1]:
                raise ValueError('Outputs mismatch')
            if layers != value[2]:
                raise ValueError('Layers mismatch')
            if neurons_per_layer != value[3]:
                raise ValueError('Neurons mismatch')
            if max_bits != value[4]:
                raise ValueError('Bits mismatch')
            if max_individuals != value[5]:
                raise ValueError('Individuals mismatch')
            if max_parents != value[6]:
                raise ValueError('Parents mismatch')
            if children_per_couple != value[7]:
                raise ValueError('Children mismatch')
            if mutation_rate != value[8]:
                raise ValueError('Mutation mismatch')
            if max_generations != value[9]:
                raise ValueError('Generations mismatch')

    except FileNotFoundError:
        create_config()

    except ValueError as e:
        print(e)
        print('A reset is needed to apply the changes')
        proceed = input('Would you like to proceed? [y/n]')

        if proceed.lower() == 'y':
            apply_conf(update_config(value))
        else:
            print('Changes won\'t be applicated')

def apply_conf(variables):
    try:
        with open('Utilities/Conf.py', 'r+') as f:
            f.seek(30)
            f.write('\n\n')
            f.writelines(variables)
            with open('GenAlg.conf', 'w') as conf_file:
                conf_file.writelines(variables)
        Console.reset()
    except FileNotFoundError:
        print('Configuration Error')

def create_config():
    print('Let\'s configurate your genetic algorithm')

    max_individuals = input('max_individuals: ')
    max_bits = int(input('max bits: '))

    variables = [
    'inputs = {}\n'.format(inputs),
    'outputs = {}\n'.format(outputs),
    'layers = {}\n'.format(layers),
    'neurons_per_layer = {}\n'.format(neurons_per_layer),
    'max_bits = {}\n'.format(max_bits),
    'max_individuals = {}\n'.format(max_individuals),
    'max_parents = {}\n'.format(max_parents),
    'children_per_couple = {}\n'.format(children_per_couple),
    'mutation_rate = {}\n'.format(mutation_rate),
    'max_generations = {}\n'.format(max_generations)
    ]

    print('Configuration ready')
    print('The program will reset to apply the changes')
    apply_conf(variables)

def update_config(values):
    return [
    'inputs = {}\n'.format(values[0]),
    'outputs = {}\n'.format(values[1]),
    'layers = {}\n'.format(values[2]),
    'neurons_per_layer = {}\n'.format(values[3]),
    'max_bits = {}\n'.format(values[4]),
    'max_individuals = {}\n'.format(values[5]),
    'max_parents = {}\n'.format(values[6]),
    'children_per_couple = {}\n'.format(values[7]),
    'mutation_rate = {}\n'.format(values[8]),
    'max_generations = {}\n'.format(values[9])
    ]
