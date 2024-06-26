# Doubling Experiment Tool Report

## Motivation 

The tool implemented here is meant to create a simple way to test the worst-case time complexity of a given sorting algorithm. The tests can be customized by starting with the size of the list and the number of runs.

## Tool Breakdown

### Files

#### Files Overview
 
Main Directory
- `main.py`
- `generate.py`
- `benchmark.py`
- `constants.py`
- `sortingfunctions.py`

Test Folder

- `generate_test.py`
- `doubling_test.py`
- `sorting_test.py`

#### Files in Detail

##### `main.py`

This file is our main control center for the output of the program using the `main` function. The command line interface is setup in this file and the output is printed in the terminal.

##### `generate.py`

This file contains multiple functions that aid in random list generation. `generate_random_number` generates a single integer between 0 and a given maximum using the `random` module. `generate_random_container_int` creates the random list with a given size utilizing the `generate_random_number` function to fill the list with as many integers as there are in the size. 

##### `benchmark.py`

The benchmark file contains all the required functions that we use to the doubling experiment. The `read_in_function_from_file` function is responsible for dynamically importing function(s) from a file given the path of the file and its name. It also makes sure that the files exists. Then we have the `double_ratio` function which does the calculation of the doubling ratio based on the last two execution times in a list. Using a simple if else statement it determines the growth pattern, if it is linear, constant or it is another growth pattern. Lastly we have the `doublingfunction` function which is the "engine" of the file. It performs a performance analysis of a sorting algorithm. It does this by running the sorting algorithm on a list of integers of increasing size and measuring the time it takes to sort the list.

##### `generate_test.py`

This file contains the test cases for the `generate.py` file. It test out all the functions inside the module, where it test the `generate_random_number()` if the random number is within or over the maximum. Another function that is being tested is the `generate_random_container_int` function that check whether the function correctly generates a list based on the given specifications.

##### `doubling_test.py`

This file contains to be the unit test for a function called `doublingfunction` within a module named `doubling.benchmark`. It test out whether the doubling function is working correctly based on the given specifications, which is the `file_name`, `function_name`, `starting_size`, and `runs`. This function is testing the doubling each iteration of the list.

##### `sorting_test.py`

This file ensures that the sorting function is implemented correctly. The function assumes that the sorting algorithms are defined elsewhere and are correctly imported at the start of the script with `from doubling import sortingfunctions`.

##### `sortingfunctions.py`

This file has contains the code for the different sorting algorithms, such as `bubble_sort`, `selection_sort`, `insertion_sort`, `merge_sort`, `quick_sort` and `python_sort`.

1. **bubble_sort**: This algorithm iterates through the list multiple times and swap them if they are in the wrong order. It would not stop until the list is sorted.

2. **selection_sort**: This algorithm divides the input list into halves: the sorted sublist and the unsorted sublist. Each iteration of the list selects the smallest element from the unsorted sublist and swap it with the leftmost unsorted element, expanding the sorted sublist.

3. **insertion_sort**: This algorithm builds the final sorted list by iterating one item at a time. It is taking the next element from the unsorted position and inserting it to the correct position in the sorted part.

4. **merge_sort**: This function implements the merge sort algorithm. It recursively divides the input list into halves until each sublist contains only one element. Then, it merges the sublists in a sorted manner, combining them into larger sorted sublists until the entire list is sorted.

5. **quick_sort**: This function implements the quick sort algorithm. It selects a pivot element from the list and partitions the other elements into two sublists according to whether they are less than or greater than the pivot. It then recursively sorts the sublists. This algorithm selects an pivot element from the list and separates the other elements to 2 sublists based on whether they are less than or greater than the pivot.

6. **python_sort**: This algorithm uses Python's built-in `sorted()` function to sort the input list.

### Input & Output


#### Bubble Sort input:

`poetry run doubling --starting-size 1000 --runs 5 --file_path sortingfunctions.py --sorting-algorithm bubble_sort`

```text
Number of runs: 5
File Path: sortingfunctions.py
Sorting algorithm: selection_sort
Run 1 of 5 for selection_sort operation with a list size of 1000 took 0.0121803284 seconds
Run 2 of 5 for selection_sort operation with a list size of 2000 took 0.0508677959 seconds
Run 3 of 5 for selection_sort operation with a list size of 4000 took 0.1876626015 seconds
Run 4 of 5 for selection_sort operation with a list size of 8000 took 0.7470493317 seconds
Run 5 of 5 for selection_sort operation with a list size of 16000 took 3.0009748936 seconds

Behold the worst-case time complexity analysis!
The ratio was 4.01710404689 which rounds to 4 which means that the worst-case time complexity is likely quadratic or worse!
```

#### Selection Sort input:

`poetry run doubling --starting-size 1000 --runs 5 --file_path sortingfunctions.py --sorting-algorithm selection_sort`

```text
Starting size: 1000
Number of runs: 5
File Path: sortingfunctions.py
Sorting algorithm: selection_sort
Run 1 of 5 for selection_sort operation with a list size of 1000 took 0.0140030384 seconds
Run 2 of 5 for selection_sort operation with a list size of 2000 took 0.0484406948 seconds
Run 3 of 5 for selection_sort operation with a list size of 4000 took 0.1885452271 seconds
Run 4 of 5 for selection_sort operation with a list size of 8000 took 0.7483632565 seconds
Run 5 of 5 for selection_sort operation with a list size of 16000 took 2.9773070812 seconds

Behold the worst-case time complexity analysis!
The ratio was 3.97842498992 which rounds to 4 which means that the worst-case time complexity is likely quadratic or worse!
```

#### Insertion Sort input:

`poetry run doubling --starting-size 1000 --runs 5 --file_path sortingfunctions.py --sorting-algorithm insertion_sort`

```
Starting size: 1000
Number of runs: 5
File Path: sortingfunctions.py
Sorting algorithm: insertion_sort
Run 1 of 5 for insertion_sort operation with a list size of 1000 took 0.0130105019 seconds
Run 2 of 5 for insertion_sort operation with a list size of 2000 took 0.0498890877 seconds
Run 3 of 5 for insertion_sort operation with a list size of 4000 took 0.1984264851 seconds
Run 4 of 5 for insertion_sort operation with a list size of 8000 took 0.7884969711 seconds
Run 5 of 5 for insertion_sort operation with a list size of 16000 took 3.2496039867 seconds

Behold the worst-case time complexity analysis!
The ratio was 4.12126375345 which rounds to 4 which means that the worst-case time complexity is likely quadratic or worse!
```

#### Merge Sort input:

`poetry run doubling --starting-size 1000 --runs 5 --file_path sortingfunctions.py --sorting-algorithm merge_sort`

```
Starting size: 1000
Number of runs: 5
File Path: sortingfunctions.py
Sorting algorithm: merge_sort
Run  1 of  5 for merge_sort operation with a list size of 1000 took 0.0080037117 seconds   
Run  2 of  5 for merge_sort operation with a list size of 2000 took 0.0049836636 seconds   
Run  3 of  5 for merge_sort operation with a list size of 4000 took 0.0179569721 seconds
Run  4 of  5 for merge_sort operation with a list size of 8000 took 0.0311799049 seconds
Run  5 of  5 for merge_sort operation with a list size of 16000 took 0.0462493896 seconds

Behold the worst-case time complexity analysis!
The ratio was 1.4833075899616144 which rounds to 1 which means that the worst-case time complexity is likely logarithmic!
```

#### Quick Sort input:

`poetry run doubling --starting-size 1000 --runs 5 --file_path sortingfunctions.py --sorting-algorithm quick_sort`

```text
Starting size: 1000
Number of runs: 5
File Path: sortingfunctions.py
Sorting algorithm: quick_sort
Run  1 of  5 for quick_sort operation with a list size of 1000 took 0.0009956360 seconds   
Run  2 of  5 for quick_sort operation with a list size of 2000 took 0.0020067692 seconds   
Run  3 of  5 for quick_sort operation with a list size of 4000 took 0.0030019283 seconds   
Run  4 of  5 for quick_sort operation with a list size of 8000 took 0.0070052147 seconds
Run  5 of  5 for quick_sort operation with a list size of 16000 took 0.0100560188 seconds

Behold the worst-case time complexity analysis!
The ratio was 1.435504730787557 which rounds to 1 which means that the worst-case time complexity is likely logarithmic!
```

#### Python Sort input:


`poetry run doubling --starting-size 1000 --runs 5 --file_path sortingfunctions.py --sorting-algorithm python_sort`

```text
Starting size: 1000
Number of runs: 5
File Path: sortingfunctions.py
Sorting algorithm: python_sort
Run 1 of 5 for python_sort operation with a list size of 1000 took 0.0000572205 seconds
Run 2 of 5 for python_sort operation with a list size of 2000 took 0.0001194477 seconds
Run 3 of 5 for python_sort operation with a list size of 4000 took 0.0002787113 seconds
Run 4 of 5 for python_sort operation with a list size of 8000 took 0.0004899502 seconds
Run 5 of 5 for python_sort operation with a list size of 16000 took 0.0026359558 seconds

Behold the worst-case time complexity analysis!
The ratio was 5.38004842125 which rounds to 5. This is indicative of some other growth pattern. Try again with more runs to get more details!"
```


### Data Tables and Graphs

![image](https://github.com/PCain02/all_hands_group2_doublingtool/assets/82393336/45957809-e820-40c7-9727-688f0f18a58a)

### Conclusion

In conclusion, for sorting large lists, it's more efficient to implement sorting algorithms with a time complexity of O(log n), just like merge sort and quick sort, or just using the sorting function that is built in Python programming language. Algorithms with a time complexity of O(n^2), like Selection Sort and Insertion Sort, are less efficient for larger list sizes. It is also important to mention that at low input sizes tasks running in the background can affect the result or different computers will do different results as well since the configuration is not the same for every one of them. In our analysis we tried to run the experiments in the same situation every time we ran the code.
