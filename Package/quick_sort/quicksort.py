def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    i, j = left, right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if left < j:
        quicksort(arr, left, j)
    if i < right:
        quicksort(arr, i, right)
    return arr 