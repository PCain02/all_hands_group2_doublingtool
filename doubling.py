from algorithims import approach, functioncall, sortingfunctions
import generate
import time


# file_path: str,
# function_name: str,
def doubling(
    starting_size: int,
    runs: int,
    sorting_algorithm: str,
):
    """Run the doubling experiment on a given function in a specified file path."""
    execution_times = []
    # TODO: ADD READING IN OF FILE AND FUNCTION
    for _ in range(1, runs + 1):
        # makes container
        generated_list = generate.generate_random_container_int(starting_size, 1000)
        # gets the list from the called function
        # list_result = functioncall.find_function_in_file(file_path, function_name)
        # Checks the list for strings
        # string_check = functioncall.check_for_str(list_result)
        start_time = time.time()
        # takes a sorting algo and a list and sorts it.
        sorted_result = functioncall.sort_list(sorting_algorithm, generated_list)
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

def double_ratio(execution_times):
    """Calculate the doubling ratio from the last two execution times in a list"""
    # Ensure there are at least two execution times to calculate a ratio
    if len(execution_times) < 2:
        print("Not enough data to calculate doubling ratios.")
        return None
    # Calculate the doubling ratio from the last two execution times and round it
    n = round(execution_times[-1] / execution_times[-2])
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

