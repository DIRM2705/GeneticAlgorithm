from Utilities import Conf

def To_bin(number : int) -> str: #Convert decimals to binary number (in string)
    binNumber = '' #Auxiliar variable

    for i in range(Conf.max_bits, -1, -1):
        bitValue = 2**i #
        if number >= bitValue:
            binNumber += '1'
            number -= bitValue
        else:
            binNumber += '0'

    return binNumber

def To_dec(number :str) -> int:
    decNumber = 0

    i = Conf.max_bits
    for char in number:
        if char == '1':
            decNumber += 2**i
        i -= 1
    return decNumber
