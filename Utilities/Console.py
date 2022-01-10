import os
import time
import sys

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def reset():
    print('resetting in...')
    for i in range(3, 0, -1):
        print('{}...'.format(i))
        time.sleep(1)
    print('resetting')

    os.execl(sys.executable, sys.executable, 'Main.py')
