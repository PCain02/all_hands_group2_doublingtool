from doubling.sortingfunctions import Sortingalgorithms


# The function correctly sorts a list of integers in ascending order using the specified sorting approach.
def test_sort_list_sorts_list_in_ascending_order():
    # Arrange
    input_list = [4, 2, 1, 3]
    expected_output = [1, 2, 3, 4]

    # Act
    bubble_output = Sortingalgorithms.bubblesort, input_list
    bubble_stopearly_output = Sortingalgorithms.bubblesort_stopearly(input_list)
    insertion_output = Sortingalgorithms.insertionsort(input_list)
    mergesort_output = Sortingalgorithms.mergesort(input_list)
    pythonsort_output = Sortingalgorithms.python_sort(input_list)
    selectionsort_output = Sortingalgorithms.selectionsort(input_list)

    # Assert
    assert bubble_output == expected_output
    assert bubble_stopearly_output == expected_output
    assert insertion_output == expected_output
    assert mergesort_output == expected_output
    assert pythonsort_output == expected_output
    assert selectionsort_output == expected_output
