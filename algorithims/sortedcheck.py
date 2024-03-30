# takes a list


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
