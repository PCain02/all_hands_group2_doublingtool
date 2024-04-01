from sortingfunctions import Sortingalgorithms
from approach import Sortingapproach
from typing import List
import importlib.util

# I currently have the
# takes sorting function and list


def sort_list(sorting_algo, input_list: List[int]) -> List[int]:
    """Sort the input list using the specified sorting approach."""
    if sorting_algo == Sortingapproach.bubblesort:
        return Sortingalgorithms.bubblesort(input_list)
    elif sorting_algo == Sortingapproach.bubblesort_stopearly:
        return Sortingalgorithms.bubblesort_stopearly(input_list)
    elif sorting_algo == Sortingapproach.insertionsort:
        return Sortingalgorithms.insertionsort(input_list)
    elif sorting_algo == Sortingapproach.mergesort:
        return Sortingalgorithms.mergesort(input_list)
    elif sorting_algo == Sortingapproach.pythonsort:
        return Sortingalgorithms.python_sort(input_list)
    elif sorting_algo == Sortingapproach.selectionsort:
        return Sortingalgorithms.selectionsort(input_list)
    else:
        raise ValueError("Invalid sorting approach")


def find_function_in_file(file_path, function_name):
    try:
        with open(file_path, "r") as file:
            for line in file:
                if function_name in line:
                    if line.strip().startswith("def " + function_name + "("):
                        return function_name
        print("Function '{}' not found in file '{}'".format(function_name, file_path))
        return None

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage:
file_path = "testl.py"
function_name = "make_list"
found_function_name = find_function_in_file(file_path, function_name)
if found_function_name:
    print(f"Function '{function_name}' found in file '{file_path}'.")

    try:
        module = importlib.import_module(file_path[:-3].replace("\\", "."))
        found_function = getattr(module, found_function_name)
        result = found_function()

    except Exception as e:
        print(f"Error calling the function: {e}")
else:
    print(f"Function '{function_name}' not found in file '{file_path}'.")
