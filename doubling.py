<<<<<<< HEAD
from algorithims import approach, functioncall, sortingfunctions
import generate
import time


def doubling(
    file_path: str,
    function_name: str,
    starting_size: int,
    runs: int,
    sorting_algorithm: str,
):
    """Run the doubling experiment on a given function in a specified file path."""
    execution_times = []
    # TODO: ADD READING IN OF FILE AND FUNCTION
    for _ in range(runs):
        # makes container
        generated_list = generate.generate_random_container(starting_size)
        # gets the list from the called function
        list_result = functioncall.find_function_in_file(file_path, function_name)
        # Checks the list for strings
        string_check = functioncall.check_for_str(list_result)
        start_time = time.time()
        sorted_result = functioncall.sort_list(sorting_algorithm, string_check)
        end_time = time.time()
        execution_time = end_time - start_time
        results = [
            execution_time,
            sorting_algorithm,
        ]
        print(
            f"Run {_} of {runs} for {sorting_algorithm} operation with a list size of {starting_size} took {execution_time:.10f} seconds"
        )
        execution_times.append(results)
        starting_size *= 2

    return execution_times
=======
>>>>>>> a8a2834dc9150d4ea9717f8ad96f6baea6fbf251
