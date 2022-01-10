def config():
    try:
        with open('Algoritmo Genético.conf', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('file not found')

        #max_individuals = input('max_individuals: ')

        #max_bits = int(input('max bits: '))
        #max_bits -= 1

        #with open('Extentions/Convertion_extentions.py', 'r+') as f:

            #f.seek(0)
            #f.write('max_bits : int = {} #Maximum amount of bits'.format(max_bits))
