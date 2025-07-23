def selection_sort(arr):
    """
    Performs an in-place selection sort on the array.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print("hello again")