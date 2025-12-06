def bubble_sort(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array