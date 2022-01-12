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

def wait_for_key():
    if os.name == 'nt':
        os.system('pause')
    elif os.name == 'posix':
        os.system('read -s -n 1 -p "Press any key to continue..."')
