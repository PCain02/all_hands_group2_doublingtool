from enum import Enum


class Sortingapproach(str, Enum):
    """Defines the approaches"""

    bubblesort = "bubblesort"
    bubblesort_stopearly = "bubblesort_stopearly"
    insertionsort = "insertionsort"
    mergesort = "mergesort"
    pythonsort = "pythonsort"
    selectionsort = "selectionsort"

    def __str__(self):
        return self.value