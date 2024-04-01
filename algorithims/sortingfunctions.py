# All of the sorting functions
# All functions take a list as input
# I may try and use regx to handle strings


class Sortingalgorithms:
    def __init__(self, list_of_values: list) -> None:
        self.list_of_values = list_of_values

    def bubblesort(L: list):
        for _ in range(len(L) - 1):
            for i in range(len(L) - 1):
                if L[i] > L[i + 1]:
                    L[i], L[i + 1] = L[i + 1], L[i]

    def bubblesort_stopearly(L: list):
        keepgoing = True
        while keepgoing:
            keepgoing = False
            for i in range(len(L) - 1):
                if L[i] > L[i + 1]:
                    L[i], L[i + 1] = L[i + 1], L[i]
                    keepgoing = True

    def insertionsort(L: list):
        n = len(L)
        for i in range(n):
            j = n - i - 1
            while j < n - 1 and L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                j += 1

    def mergesort(self) -> None:
        """Implement Merge Sort algorithm."""

        def merge_sort_helper(L):
            if len(L) < 2:
                return
            mid = len(L) // 2
            A = L[:mid]
            B = L[mid:]
            merge_sort_helper(A)
            merge_sort_helper(B)
            self._merge(A, B, L)

        merge_sort_helper(self.list_of_values)

    def _merge(self, A, B, L) -> None:
        """Merge two sorted lists A and B into L."""
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                L[i + j] = A[i]
                i = i + 1
            else:
                L[i + j] = B[j]
                j = j + 1
        L[i + j :] = A[i:] + B[j:]

    def python_sort(x: list[int]) -> list:
        sorted_list = sorted(x)
        return sorted_list

    def selectionsort(L) -> list:
        n = len(L)
        for i in range(n - 1):
            max_index = 0
            for index in range(n - i):
                if L[index] > L[max_index]:
                    max_index = index
            L[n - i - 1], L[max_index] = L[max_index], L[n - i - 1]
        return L

    # Just putting these here just incase we want to do something with them
    def issorted(L):
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                return False
        return True

    def issorted_allpairs(L):
        for i in range(len(L) - 1):
            for j in range(i + 1, len(L)):
                if L[j] < L[i]:
                    return False
        return True
