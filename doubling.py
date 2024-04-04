import time
from typing import List, Tuple, Union

def doubling(file_name: str, function_name: str, starting_size: int, runs: int) -> Tuple[List[float], List[int]]:
  """Run the doubling experiment on a given function in a specified file path."""
  execution_times = []
  # TODO: ADD READING IN OF FILE AND FUNCTION
  for run_number in range(runs):
    generated_list = generate.generate_random_container(starting_size, 100)
    start_time = time.time()
    result = getattr(generated_list, file.function_name)()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Run {run_number+1} of {runs} for {operation} operation with list using size {starting_size} took {execution_time:.10f} seconds")
    execution_times.append((run_number, starting_size, execution_time))
    starting_size *= 2 
  return execution_times
