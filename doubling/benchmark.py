import generate
#from constants import DoublingBenchmarkValues
#from doubling import constants
import time
from typing import List


#doubling_benchmark_values = constants.DoublingBenchmarkValues

# file_path: str,
# function_name: str,

def read_in_function_from_file(file_path: str, function_name: str):
    with open(file_path, 'r') as file:
        code = compile(file.read(), file_path, 'exec')
        exec(code, globals())
        # Get the globals in the file
        mod = globals()
        if function_name in mod:
            return mod[function_name]
        else:
            raise AttributeError(f"Function not found!")

        
def double_ratio(execution_times: List[float]) -> None: 
    """Calculate the doubling ratio from the last two execution times in a list"""
    # Ensure there are at least two execution times to calculate a ratio
    if len(execution_times) < 2:
        print("Not enough data to calculate doubling ratios.")
        return None
    # Calculate the doubling ratio from the last two execution times and round it
    n = round(float(execution_times[1]) / float(execution_times[0]))
    # Determine the growth pattern based on the rounded doubling ratio
    if n == 1:
        print("Constant")
        return 1
    elif n == 2:
        print("Linear")
        return 2
    else:
        print("Other growth pattern")
        return n
    return None

def doublingfunction(
    starting_size: int,
    runs: int,
    file_path: str,
    sorting_algorithm: str,
):
    """Run the doubling experiment on a given function in a specified file path."""
    execution_times = []
    results_list = []
    selected_function = read_in_function_from_file(file_path, sorting_algorithm)
    for _ in range(1, runs + 1):
        # makes container
        generated_list = generate.generate_random_container_int(starting_size, 100)
        # gets the list from the called function
        # list_result = functioncall.find_function_in_file(file_path, function_name)
        # Checks the list for strings
        # string_check = functioncall.check_for_str(list_result)
        start_time = time.time()
        # takes a sorting algo and a list and sorts it.
        sorted_result = selected_function(generated_list)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(float(execution_time))
        results = [
            execution_time,
            sorting_algorithm,
        ]
        print(
            f"Run {_} of {runs} for {sorting_algorithm} operation with a list size of {starting_size} took {execution_time:.10f} seconds"
        )
        results_list.append(results)
        starting_size *= 2
    double_ratio(execution_times)
    return results_list