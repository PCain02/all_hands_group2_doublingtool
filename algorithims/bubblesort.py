import sortedcheck


def bubblesort(L):
    for _ in range(len(L) - 1):
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]


data = [30, 100000, 54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Is the data sorted?", sortedcheck.issorted(data))
print(data)
bubblesort(data)
print("Is the data sorted?", sortedcheck.issorted(data))
print(data)
