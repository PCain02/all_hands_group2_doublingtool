"""Generate random data values and collections as containers."""

import random
from typing import List, Tuple, Union


def generate_random_number(maximum: int) -> int:
    """Generate a random number either up to the maximum or exceeding it by one and return it."""
    # generate a random number that is either up to the maximum
    # or exceeding it by one, depending on the input parameter values
    num = random.randint(0, maximum)
    return num

def generate_random_str()-> str:
    """Generate a random string based on the alphabet."""
    list_of_str = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num = random.randint(0, 25)
    return list_of_str[num]

def generate_random_container_int(
    size: int, maximum: int
) -> List:
    """Generate a container of a specified size filled with random numbers up to a certain maximum and return either a list or a tuple."""
    #  generate a list of random values for a specific size
    # and with a number up to a specific maximum
    random_list = []
    for i in range(size):
        num = generate_random_number(maximum)
        random_list.append(num)
    return random_list

def generate_random_container_str(
    size: int
) -> List:
    """Generate a container of a specified size filled with random numbers up to a certain maximum and return either a list or a tuple."""
    #  generate a list of random values for a specific size
    # and with a number up to a specific maximum
    random_list = []
    for i in range(size):
        letter = generate_random_str()
        random_list.append(letter)
    return random_list
