<<<<<<< Updated upstream
import random

def heapify(A, n, i):
    largest = i     #Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    #See if left child of root exists and is > root
    if l < n and A[largest] < A[l]:
        largest = l
    
    #See if right child of root exists and is > root
    if r < n and A[largest] < A[r]:
        largest = r
    
    #Change root, if needed
    if largest != i:
        A[i], A[largest] = A[largest], A[i] #Swap

        #Heapify the root
        heapify(A, n, largest)

def heapSort(A):
    n = len(A)

    #Build a max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)
    
    #One by one extract elements
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i] #Swap
        heapify(A, i, 0)

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
=======
import math

def sort(arrayA):
    maxdepth = (math.log(len(arrayA))) * 2
    introsort(arrayA, maxdepth)

def introsort(sampleArray, )
>>>>>>> Stashed changes
