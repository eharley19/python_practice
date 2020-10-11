from random import randint

from ls16 import convert_to_list


T3_STRING_LENGTH = 5
T2_MAX_STRING_LENGTH = 500


def t2_sample_generator(size):
    for _ in range(size):
        str_length = randint(1, T2_MAX_STRING_LENGTH)
        new_string = ''.join(chr(randint(ord('!'), ord('~'))) for x in range(str_length))
        yield new_string


def t3_sample_generator(size):
    for _ in range(size):
        new_string = "".join(chr(randint(ord('a'), ord('z'))) for x in range(T3_STRING_LENGTH))
        yield new_string


def t4_sample_generator(size):
    v = randint(0, 26**100 - 1)
    for i in range(size):
        o = randint(-5, 5)
        new_num = v + i + o
        new_string = convert_to_string(new_num)
        yield new_string


def convert_to_string(num: int):
    num_list = convert_to_list(num, 26)
    new_string = ''.join(chr(digit + ord("A")) for digit in num_list)
    return new_string


def create_file(generator):
    filename = input("Filename: ")
    size = 1000000
    with open(filename, 'w') as f:
        f.write(str(size) + '\n')
        for line in generator(size):
            f.write(line + '\n')


create_file(t4_sample_generator)
