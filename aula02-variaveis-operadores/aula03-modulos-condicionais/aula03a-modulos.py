import math

# print(math.sin(math.pi))

import random

num_rand = math.ceil(random.random() * 10)
num_rand_int = random.randint(0, 10)
# print(num_rand)
# print(num_rand_int)



def convert_to_binary(number: int):
    if (number == 0): return '0'

    binary = ''

    while (number >= 1):
        binary = str(number % 2) + binary
        number //= 2

    return binary

print(convert_to_binary(2))
