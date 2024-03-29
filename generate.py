"""Generate random data values and collections as containers."""

import random
from typing import List, Tuple, Union


def generate_random_number(maximum: int, exceed: bool = False) -> int:
    """Generate a random number either up to the maximum or exceeding it by one and return it."""
    # generate a random number that is either up to the maximum
    # or exceeding it by one, depending on the input parameter values
    if exceed is False:
        num = random.randint(0, maximum)
    else:
        num = maximum + 1
    return num

def generate_random_container(
    size: int, maximum: int
) -> List:
    """Generate a container of a specified size filled with random numbers up to a certain maximum and return either a list or a tuple."""
    #  generate a list of random values for a specific size
    # and with a number up to a specific maximum
    random_list = []
    for i in range(size):
        # num = generate_random_number(maximum, False)
        random_list.append(random.randint(0, maximum))
        # convert the list to a tuple if this was requested
    return random_list
