import random


def partition(A, p, r, q):
    pivot = A[q]
    tmp = []
    for i in range(p, q):
        tmp.append(A[i])
    for i in range(q + 1, r + 1):
        tmp.append(A[i])
    i = p
    j = r
    for t in tmp:
        if t <= pivot:
            A[i] = t
            i += 1
        else:
            A[j] = t
            j -= 1
    A[j] = pivot
    return j

def quicksort(A, p, r):
    if p < r:
        q = random.randrange(p, r + 1)
        new_q = partition(A, p, r, q)
        quicksort(A, p, new_q - 1)
        quicksort(A, new_q + 1, r)

def insertion_sort(lst):
    for i in range(len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key