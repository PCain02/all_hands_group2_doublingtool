import time
import pytest
from typing import List, Tuple
from doubling.benchmark import doublingfunction

def test_doubling():
    file_name = __file__
    function_name = 'doubling'
    starting_size = 10
    runs = 5

    expected_sizes = [starting_size * (2 ** i) for i in range(runs)]
    expected_times = [0.01] * runs

    actual_times, actual_sizes = doublingfunction(file_name, function_name, starting_size, runs)

    assert expected_sizes == actual_sizes
    for expected, actual in zip(expected_times, actual_times):
        assert abs(expected - actual) < 0.01