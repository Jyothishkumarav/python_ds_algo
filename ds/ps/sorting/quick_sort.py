def quick_sort(arr, low, high):
    if not arr:
        return arr
    low = 0
    high = len(arr) -1
    if low < high:
        partion_index = partion(arr, low, high)
        quick_sort(arr, low, partion_index - 1)  # Left of pivot
        quick_sort(arr, partion_index + 1, high)  # Right of pivot


def partion(arr, low, high):
    pivot = arr[high]
    left = low
    right = high -1
    while left < right:
        while left < right and arr[left] <= pivot:
            left +=1
        while left < right and arr[right] > pivot:
            right -=1
        if left < right:
            arr[left], arr[right] = arr[right] , arr[left]
    if arr[left] > pivot:
        arr[left], arr[high] = arr[high], arr[left]
        return left
    else:
        arr[left+1],arr[high] = arr[high], arr[left+1]
        return left +1
