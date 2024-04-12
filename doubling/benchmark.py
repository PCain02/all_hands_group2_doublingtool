from doubling import generate

# from constants import DoublingBenchmarkValues
# from doubling import constants
import time
from typing import List, Tuple, Callable, Any
from doubling import constants


# doubling_benchmark_values = constants.DoublingBenchmarkValues

# file_path: str,
# function_name: str,

benchmarkvalues = constants.benchmark_values


def read_in_function_from_file(file_path: str, function_name: str) -> Callable:
    """Reads and returns a function from a specified Python source file."""
    with open(file_path, "r") as file:
        code = compile(file.read(), file_path, "exec")
        exec(code, globals())
        # Get the globals in the file
        mod = globals()
        if function_name in mod:
            return mod[function_name]
        else:
            raise AttributeError(f"Function not found: {function_name}!")


def double_ratio(execution_times: List[float]) -> float:
    """Calculate the doubling ratio from the last two execution times in a list"""
    # Ensure there are at least two execution times to calculate a ratio
    print()
    print("Behold the worst-case time complexity analysis!")
    if float(execution_times[-1]) == 0.0 or float(execution_times[-2]) == 0.0:
        print("We can not divide by zero! Results are inconclusive!")
        return 0.0
    if len(execution_times) > 2:
        n = float(execution_times[-1]) / float(execution_times[-2])
        n_rounded = round(
            float(execution_times[-1]) / float(execution_times[-2])
        )
        if n < 1:
            print(
                f"The ratio was {n} which rounds to {n_rounded} which means that the worst-case time complexity is Constant or better!"
            )
        elif 1 < n < 2 and n_rounded != 2:
            print(
                f"The ratio was {n} which rounds to {n_rounded} which means that the worst-case time complexity is likely logarithmic!"
            )
            return n
        elif 1 < n < 2 and n_rounded == 2:
            print(
                f"The ratio was {n} which rounds to {n_rounded} which means that the worst-case time complexity is likely linear!"
            )
            return n
        elif n > 2 and n_rounded == 2:
            print(
                f"The ratio was {n} which rounds to {n_rounded} which means that the worst-case time complexity is likely linear!"
            )
            return n
        elif 4 > n > 2 and n_rounded != 4:
            print(
                f"The ratio was {n} which rounds to {n_rounded} which means that the worst-case time complexity is likely linearithmic or worse!"
            )
            return n
        elif n > 4 or n_rounded == 4:
            print(
                f"The ratio was {n} which rounds to {n_rounded} which means that the worst-case time complexity is likely quadratic or worse!"
            )
            return n
        else:
            print(
                f"The ratio was {n} which rounds to {n_rounded}. This is indicative of some other growth pattern. Try again with more runs to get more details!"
            )
            return n
    # Calculate the doubling ratio from the last two execution times and round it
    else: 
        print("You did not have enough runs to come up with a result! Try running again with more runs.")
    print(
        "If these aren't the expected results, try increasing the input sizes."
    )
    return 0.0


def doublingfunction(
    starting_size: int,
    runs: int,
    file_path: str,
    sorting_algorithm: str,
) -> List[Tuple[float, str]]:
    """
    Executes a sorting algorithm function specified by name, imported from a given file,
    over increasingly large random lists of integers, doubling in size with each run,
    to measure performance and compute time ratios.
    """
    execution_times = []
    results_list = []
    selected_function = read_in_function_from_file(
        file_path, sorting_algorithm
    )
    for _ in range(1, runs + 1):
        # makes container
        generated_list = generate.generate_random_container_int(
            starting_size, benchmarkvalues.min_size
        )
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
            f"Run {_:2} of {runs:2} for {sorting_algorithm:15} operation with a list size of {starting_size:10} took {execution_time:.10f} seconds"
        )
        results_list.append(results)
        starting_size *= 2
    double_ratio(execution_times)
    return results_list
