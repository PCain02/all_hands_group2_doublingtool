# all_hands_group2_doublingtool
Tool that does a doubling experiment

Link to Doc https://docs.google.com/document/d/11gcGiVxx0g4t9ZRkzyVi58d2r75RY3IWuQiaPVDlv1k/edit?usp=sharing 

# Doubling Experiment Tool Report

## Motivation 

The tool implemented here is meant to create a simple way to test the worst-case time complexity of a given sorting algorithm. The tests can be customized by starting with the size of the list and the number of runs.

## Tool Breakdown

### Files

#### Files Overview
 
 Main Directory 
- `main.py`
- `generate.py`
- `doubling.py`
- `generate_test.py`
- `doubling_test.py`
- `sorting_test.py`

Algorithms Folder
- `approach.py`
- `functioncall.py`
- `sortingfunctions.py`
- `testl.py`

#### Files in Detail

##### `main.py`

This file is our main control center for the output of the program using the `main` function. The command line interface is setup in this file and the output is printed in the terminal.

##### `generate.py`

This file contains multiple functions that aid in random list generation. `generate_random_number` generates a single integer between 0 and a given maximum using the `random` module. `generate_random_str` works in a similar way except it will return a random `str` letter from the alphabet using the `random` module as a way to select the letter from a list of letters.

`generate_random_container_int` creates the random list with a given size utilizing the `generate_random_number` function to fill the list with as many integers as there are in the size. `generate_random_container_str` works the same except it replaces the random integers with random letters.

##### `benchmark.py`

TODO:

##### `generate_test.py`

This file contains the test cases for the `generate.py` file. It test out all the functions inside the module, where it test the `generate_random_number()` if the random number is within or over the maximum. Another function that is being tested is the `generate_random_container_int` function that check whether the function correctly generates a list based on the given specifications.

##### `doubling_test.py`

This file contains to be the unit test for a function called `doublingfunction` within a module named `doubling.benchmark`. It test out whether the doubling function is working correctly based on the given specifications, which is the `file_name`, `function_name`, `starting_size`, and `runs`. This function is testing the doubling each iteration of the list.

##### `sorting_test.py`

TODO:

##### `constants.py`

TODO:

##### `sortingfunctions.py`

TODO:

### Input

Use the command line TODO:

### Operations

TODO:

### Output

TODO:
