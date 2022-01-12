from Utilities import Conf

def To_bin(number : int) -> str: #Convert decimals to binary number (in string)
    for i in range(Conf.max_bits - 1, -1, -1):
        if i == Conf.max_bits - 1:
            if number < 0:
                bin_number = '1'
                number = abs(number)
            else:
                bin_number = '0'
            continue

        bitValue = 2**i #
        if number >= bitValue:
            bin_number += '1'
            number -= bitValue
        else:
            bin_number += '0'

    return bin_number

def To_dec(number :str) -> int:
    decNumber = 0
    for bit in range(Conf.max_bits - 1, -1, -1):
        if bit == Conf.max_bits - 1:
            continue

        if number[(Conf.max_bits - 1) - bit] == '1':
            decNumber += 2**(bit)

    if number[0] == '1':
        decNumber *= -1
    return decNumber
