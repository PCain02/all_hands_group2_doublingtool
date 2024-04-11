from doubling import sortingfunctions

def test_sorting_algorithms():
    unsorted_list = [5, 3, 8, 6, 2, 7, 1, 4]
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]

    assert python_sort(unsorted_list.copy()) == sorted_list
    assert quick_sort(unsorted_list.copy()) == sorted_list
    assert merge_sort(unsorted_list.copy()) == sorted_list
    assert insertion_sort(unsorted_list.copy()) == sorted_list
    assert selection_sort(unsorted_list.copy()) == sorted_list
    assert bubble_sort(unsorted_list.copy()) == sorted_list

if __name__ == "__main__":
  test_sorting_algorithms()
