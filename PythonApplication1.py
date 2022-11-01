braille = {'a':['OX', 'XX', 'XX'], 'b':['OX', 'OX', 'XX'], 'c':['OO', 'XX', 'XX'], 'd':['OO', 'XO', 'XX'],
           'e':['OX', 'XO', 'XX'], 'f':['OO', 'OX', 'XX'], 'g':['OO', 'OO', 'XX'], 'h':['OX', 'OO', 'XX'],
           'i':['XO', 'OX', 'XX'], 'j':['XO', 'OO', 'XX'], 'k':['OX', 'XX', 'OX'], 'l':['OX', 'OX', 'OX'],
           'm':['OO', 'XX', 'OX'], 'n':['OO', 'XO', 'OX'], 'o':['OX', 'XO', 'OX'], 'p':['OO', 'OX', 'OX'],
           'q':['OO', 'OO', 'OX'], 'r':['OX', 'OO', 'OX'], 's':['XO', 'OX', 'OX'], 't':['XO', 'OO', 'OX'],
           'u':['OX', 'XX', 'OO'], 'v':['OX', 'OX', 'OO'], 'w':['XO', 'OO', 'XO'], 'x':['OO', 'XX', 'OO'],
           'y':['OO', 'XO', 'OO'], 'z':['OX', 'XO', 'OO'], '1':['OX', 'XX', 'XX'], '2':['OX', 'OX', 'XX'],
           '3':['OO', 'XX', 'XX'], '4':['OO', 'XO', 'XX'], '5':['OX', 'XO', 'XX'], '6':['OO', 'OX', 'XX'],
           '7':['OO', 'OO', 'XX'], '8':['OX', 'OO', 'XX'], '9':['XO', 'OX', 'XX'], '0':['XO', 'OO', 'XX'],
           '.':['XX', 'OO', 'XO'], ',':['XX', 'OX', 'XX'], '!':['XX', 'OO', 'OX'], '?':['XX', 'OX', 'OO'],
           ':':['XX', 'OO', 'XX'], ';':['XX', 'OX', 'OX'], '-':['XX', 'XX', 'OO'], '(':['XX', 'OO', 'OO'],
           ')':['XX', 'OO', 'OO'], '<':['OX', 'OX', 'XO'], '>':['XO', 'XO', 'OX'], '/':['XO', 'XX', 'OX'],
           "'":['XX', 'XX', 'OX'], '*':['XX', 'XO', 'OX'], '#':['XO', 'XO', 'OO'], ' ':['XX', 'XX', 'XX'],
           'Number': ['XO', 'XO', 'OO'], 'Letter': ['XX', 'XO', 'XO']}

braille_pos = {'a':"2 3 4 5 6", 'b':"3 4 5 6", 'c':"2 3 5 6", 'd':"2 3 6", 'e':"2 3 4 6", 'f':"3 5 6", 'g':"3 6", 'h':"3 4 6",
               'i':"1 3 5 6", 'j':"1 3 6", 'k':"2 4 5 6", 'l':"4 5 6", 'm':"2 5 6", 'n':"2 6", 'o':"2 4 6", 'p':"5 6",
               'q':"6", 'r':"4 6", 's':"1 5 6", 't':"1 6", 'u':"2 4 5", 'v':"4 5", 'w':"1 3",
               'x':"2 5", 'y':"2", 'z':"2 4", '1':"2 3 4 5 6", '2':"3 4 5 6", '3':"2 3 5 6", '4':"2 3 6", '5':"2 3 4 6",
               '6':"3 5 6", '7':"3 6", '8':"3 4 6", '9':"1 3 5 6", '0':"1 3 6", '.':"1 3 4", ',':"1 3 4 5 6", '!':"1 4 6",
               '?':"1 4 5", ':':"1 3 4 6", ';':"1 4 5 6", '-':"1 2 4 5", '(':"1 4", ')':"1 4", '<':"3 4 5", '>':"1 2 6",
               '/':"1 2 5 6", "'":"1 2 4 5 6", '*':"1 2 4 6", '#':"1 2", ' ':"0", 'Number':"1 2", 'Letter':"1 2 3 4"}

Input = []
Print_Input = []
position = []
num_digit = 0
num_letter = 0

Input = list(input())

for k in Input:
    if k.isdigit():
        num_letter = 0
        if num_digit == 0:
            Print_Input.append('Number')
            num_digit = 1
    else:
        num_digit = 0
        if num_letter == 0:
            Print_Input.append('Letter')
            num_letter = 1
    Print_Input.append(k)
print(Print_Input,'\n')

num_digit = 0
num_letter = 0

for j in Input:
    if j.isdigit():
        num_letter = 0
        if num_digit == 0:
            position.append(braille_pos.get('Number'))
            num_digit = 1
    else:
        num_digit = 0
        if num_letter == 0:
            position.append(braille_pos.get('Letter'))
            num_letter = 1
    position.append(braille_pos.get(j))
print(' 0 '.join(position),'\n')

num_digit = 0
num_letter = 0

for i in Input:
    if i.isdigit():
        num_letter = 0
        if num_digit == 0:
            num_digit = 1
            for n in braille.get('Number'):
                print(n)
            print(' ')
    else:
        num_digit = 0
        if num_letter == 0:
            num_letter = 1
            for n in braille.get('Letter'):
                print(n)
            print(' ')
    for n in braille.get(i):
        print(n)
    print(' ')
Input = []
Print_Input = []
position = []
num_digit = 0
num_letter = 0

Input = list(input())

for k in Input:
    if k.isdigit():
        num_letter = 0
        if num_digit == 0:
            Print_Input.append('Number')
            num_digit = 1
    else:
        num_digit = 0
        if num_letter == 0:
            Print_Input.append('Letter')
            num_letter = 1
    Print_Input.append(k)
print(Print_Input,'\n')

num_digit = 0
num_letter = 0

for j in Input:
    if j.isdigit():
        num_letter = 0
        if num_digit == 0:
            position.append(braille_pos.get('Number'))
            num_digit = 1
    else:
        num_digit = 0
        if num_letter == 0:
            position.append(braille_pos.get('Letter'))
            num_letter = 1
    position.append(braille_pos.get(j))
print(' 0 '.join(position),'\n')

num_digit = 0
num_letter = 0

for i in Input:
    if i.isdigit():
        num_letter = 0
        if num_digit == 0:
            num_digit = 1
            for n in braille.get('Number'):
                print(n)
            print(' ')
    else:
        num_digit = 0
        if num_letter == 0:
            num_letter = 1
            for n in braille.get('Letter'):
                print(n)
            print(' ')
    for n in braille.get(i):
        print(n)
    print(' ')