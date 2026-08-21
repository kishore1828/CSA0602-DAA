def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


n = 5
arr = [10, 20, 30, 40, 50]
key = 30

position = binary_search(arr, key)

if position != -1:
    print("Element found at position", position + 1)
else:
    print("Element not found")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [2, 4, 6, 8, 10, 12]
target = 8

index = binary_search(arr, target)

print("Index =", index)

def binary_search_iterations(arr, key):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            return True, iterations

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return False, iterations


arr = [5, 10, 15, 20, 25, 30, 35]
key = 25

found, iterations = binary_search_iterations(arr, key)

if found:
    print("Element found")
else:
    print("Element not found")

print("Iterations =", iterations)

def first_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            high = mid - 1

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return result


arr = [1, 2, 2, 2, 3, 4, 5, 6]
key = 2

index = first_occurrence(arr, key)

if index != -1:
    print("First occurrence at index", index)
else:
    print("Element not found")

def last_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return result


arr = [1, 2, 2, 2, 3, 4, 5, 6]
key = 2

index = last_occurrence(arr, key)

if index != -1:
    print("Last occurrence at index", index)
else:
    print("Element not found")

def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return minimum, maximum


temperatures = [32, 28, 35, 25, 31, 29, 37]

minimum, maximum = find_min_max(
    temperatures, 0, len(temperatures) - 1
)

print("Minimum Temperature =", minimum)
print("Maximum Temperature =", maximum)

def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    return (
        min(left_min, right_min),
        max(left_max, right_max)
    )


marks = [78, 92, 65, 88, 95, 72, 81, 69]

minimum, maximum = find_min_max(
    marks, 0, len(marks) - 1
)

print("Minimum Mark =", minimum)
print("Maximum Mark =", maximum)

def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return (
            min(arr[low], arr[high]),
            max(arr[low], arr[high])
        )

    mid = (low + high) // 2

    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    return (
        min(left_min, right_min),
        max(left_max, right_max)
    )


prices = [450, 520, 480, 610, 430, 590]

minimum, maximum = find_min_max(
    prices, 0, len(prices) - 1
)

print("Minimum Stock Price =", minimum)
print("Maximum Stock Price =", maximum)

def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return (
            min(arr[low], arr[high]),
            max(arr[low], arr[high])
        )

    mid = (low + high) // 2

    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return minimum, maximum


times = [14, 12, 18, 11, 15, 13, 17, 16, 10]

minimum, maximum = find_min_max(
    times, 0, len(times) - 1
)

print("Fastest Time =", minimum)
print("Slowest Time =", maximum)

def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return (
            min(arr[low], arr[high]),
            max(arr[low], arr[high])
        )

    mid = (low + high) // 2

    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    return (
        min(left_min, right_min),
        max(left_max, right_max)
    )


heights = [120, 150, 98, 175, 140, 165, 110, 190, 130, 145]

minimum, maximum = find_min_max(
    heights, 0, len(heights) - 1
)

print("Minimum Height =", minimum)
print("Maximum Height =", maximum)
