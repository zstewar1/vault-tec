#!/usr/bin/env python3

import sys
import time

color_escapes = {
    'red': '1',
    'yellow': '3',
    'green': '2',
    'blue': '4',
    'magenta': '5',
    'cyan': '6',
    'white': '7',
    'black': '0',
}

def colorize(color, type=3):
    if color not in color_escapes:
        raise ValueError('Invalid Color')
    sys.stdout.write('\x1b[' + str(type) + color_escapes[color] + 'm')

def cls():
    sys.stdout.write('\x1b[2J\x1b[H')

def init():
    print(
        'WELCOME TO THE VAULT-TEC (TM) HACKING ASSISTANCE MODULE (V.H.A.M)\n'
        'INITIALIZING...')
    time.sleep(1)

    print('\n\nLOADING COLORIZATION MODULE (GREEN)...')
    time.sleep(.1)
    print('ALLOCATING WORD SPACE...')
    time.sleep(.1)
    print('PREPARING COUNTERS...')
    time.sleep(.1)
    print('LOADING ROBOCO INDUSTRIES (TM) TERMLINK PROTOCOL CRACKER...')
    time.sleep(1)
    print()

def get_int(message=''):
    num = None
    while num is None:
        try:
            print(message.upper())
            num = int(input('> '))
        except ValueError:
            pass
    time.sleep(.1)
    return num

def get_pass(count, message=''):
    pw = None
    while not pw or len(pw) != count:
        print(message.upper())
        pw = input('> ').upper()
    time.sleep(.1)
    return pw

def get_yn(message):
    yn = None
    while yn != 'Y' and yn != 'N':
        print(message.upper())
        yn = input('> ').upper()
    time.sleep(.1)
    return yn == 'Y'

def heading(count, attempts):
    cls()
    print('VAULT-TEC (TM) V.H.A.M. FOR TERMLINK PROTOCOL')
    print('CRACKING', count, 'CHARACTER PASSWORD\n')
    print(attempts, 'ATTEMPT(S) LEFT:', *list('\u25A0' * attempts))
    print()

def match_count(str1, str2):
    return sum(a == b for a, b in zip(str1, str2))

def main():
    colorize('green')
    cls()
    try:
        init()
    except KeyboardInterrupt:
        print()

    char_count = get_int('ENTER CHARACTER COUNT...')

    attempts = {}

    heading(char_count, 4)
    pw = get_pass(char_count, 'PLEASE SELECT A RANDOM PASSWORD FOR INITIAL TEST.')
    print(
        '\nENTER PASSWORD INTO TERMLINK CONSOLE AND REPORT THE NUMBER OF CHARACTERS '
        'CORRECT')
    correct = get_int('ENTER NUMBER OF CHARACTERS CORRECT')

    attempts[pw] = correct

    for attempt in range(3, 0, -1):
        heading(char_count, attempt)

        if attempt == 1:
            print('WARNING: 1 ATTEMPT LEFT. REBOOT RECOMMENDED.')

        print(
            'SELECT ANOTHER PASSWORD TO TEST\n'
            'DO NOT ENTER PASSWORD IN TERMLINK CONSOLE UNTIL INSTRUCTED TO DO SO')
        valid = False
        while not valid:
            pw = get_pass(char_count, 'ENTER CHOSEN PASSWORD')
            valid = True
            for opw in attempts:
                mc = match_count(pw, opw)
                if mc != attempts[opw]:
                    print('PASSWORD SELECTION INVALID. CHOOSE A DIFFERENT PASSWORD')
                    valid = False
                    break
            if valid:
                print('\nSELECTION VALID')
                valid = get_yn('USE SELECTION? (Y/N)')

        if attempt != 1:
            print(
                '\nSELECTION VALID. ENTER PASSWORD IN TERMLINK CONSOLE NOW')
            correct = get_int('ENTER NUMBER OF CHARACTERS CORRECT')
            attempts[pw] = correct
        else:
            print(
                'SELECTION VALID. ENTER THE PASSWORD IN TERMLINK CONSOLE NOW OR REBOOT '
                'TO AVOID LOCKOUT')


if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2 and sys.argv[1] == '-l':
            while True:
                try:
                    main()
                except EOFError:
                    print()
        else:
            main()
    except KeyboardInterrupt:
        print('\nGOODBYE.')
