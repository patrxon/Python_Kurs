def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    start = arr[0]
    tail = arr[1:]
    return quick_sort([x for x in tail if x < start]) + [start] + quick_sort([x for x in tail if x >= start])


print(quick_sort([3, 2, 1, 4, 5, 6]))
