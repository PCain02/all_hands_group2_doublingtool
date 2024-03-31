from sortingfunctions import Sortingalgorithms
from approach import Sortingapproach
from typing import List

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
