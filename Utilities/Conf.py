from Utilities import Console

inputs = 1
outputs = 1
layers = 2
neurons_per_layer = 3
max_bits = 7


max_individuals = 100
max_parents = 2
childs_per_couple = 5
mutation_rate = 5

def config():
    Console.clear()
    try:
        with open('Algoritmo Genético.conf', 'r') as f:
            print(f.readlines())
    except FileNotFoundError:
        print('file not found')

        max_individuals = input('max_individuals: ')
        max_bits = int(input('max bits: '))
        max_bits -= 1

        try:
            variables = [
            '\n',
            '\n',
            'inputs = {}\n'.format(inputs),
            'outputs = {}\n'.format(outputs),
            'layers = {}\n'.format(layers),
            'neurons_per_layer = {}\n'.format(neurons_per_layer),
            'max_bits = {}\n'.format(max_bits),
            '\n',
            '\n',
            'max_individuals = {}\n'.format(max_individuals),
            'max_parents = {}\n'.format(max_parents),
            'childs_per_couple = {}\n'.format(childs_per_couple),
            'mutation_rate = {}\n'.format(mutation_rate),
            '\n'
            ]

            with open('Utilities/Conf.py', 'r+') as f:
                f.seek(30)
                f.writelines(variables)
                with open('Algoritmo Genético.conf', 'w') as conf_file:
                    conf_file.writelines(variables)
                Console.reset()
        except FileNotFoundError:
            print('Configuration Error')

    print('configuration ready')
