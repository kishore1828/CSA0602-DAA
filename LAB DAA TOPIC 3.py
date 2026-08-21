arr = [12, 25, 8, 45, 32, 19, 50]
key = 32

comparisons = 0
position = -1

for i in range(len(arr)):
    comparisons += 1

    if arr[i] == key:
        position = i + 1
        break

if position != -1:
    print("Element found at position", position)
else:
    print("Element not found")

print("Number of comparisons =", comparisons)

arr = [5, 10, 15, 20, 25, 30, 35]
key = 18

comparisons = 0
found = False

for value in arr:
    comparisons += 1

    if value == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")

print("Number of comparisons =", comparisons)

arr = [10, 25, 15, 25, 30, 25, 40]
key = 25

for i in range(len(arr)):
    if arr[i] == key:
        print("First occurrence at position", i + 1)
        break

arr = [7, 12, 7, 25, 18, 7, 30, 7]
key = 7

positions = []

for i in range(len(arr)):
    if arr[i] == key:
        positions.append(i + 1)

print("Occurrences at positions:")
print(*positions, sep=", ")
print("Total occurrences =", len(positions))

arr = [3, 6, 9, 12, 15, 18, 21]
key = 15

comparisons = 0
matches = 0
mismatches = 0

for value in arr:
    comparisons += 1

    if value == key:
        matches += 1
        break
    else:
        mismatches += 1

print("Total comparisons =", comparisons)
print("Total matches =", matches)
print("Total mismatches =", mismatches)

def ordinary_search(arr, key):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == key:
            return i + 1, comparisons

    return -1, comparisons


def sentinel_search(arr, key):
    data = arr.copy()
    n = len(data)

    if n == 0:
        return -1, 0

    last = data[-1]
    data[-1] = key

    i = 0
    comparisons = 0

    while data[i] != key:
        comparisons += 1
        i += 1

    comparisons += 1

    data[-1] = last

    if i < n - 1 or data[-1] == key:
        return i + 1, comparisons

    return -1, comparisons


arr = [14, 9, 22, 35, 18, 41, 27]
key = 18

position, comparisons = sentinel_search(arr, key)

print("Position found =", position)
print("Comparison count =", comparisons)

register_numbers = [101, 102, 103, 104, 105, 106]
key = 104

for i in range(len(register_numbers)):
    if register_numbers[i] == key:
        print("Register Number found at position", i + 1)
        break
names = ["Anu", "Bala", "Charan", "Deepa", "Esha", "Farhan"]
key = "Deepa"

for i in range(len(names)):
    if names[i] == key:
        print("Name found at position", i + 1)
        break

matrix = [
    [12, 8, 15],
    [5, 18, 27],
    [9, 11, 24]
]

key = 24
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == key:
            print("Element found at Row", i + 1, "Column", j + 1)
            found = True
            break

    if found:
        break

arr = [
    45, 23, 67, 12, 89,
    34, 56, 78, 90, 11,
    29, 73, 18, 64, 37
]

keys = [73, 18, 100]

for key in keys:
    print("\nSearching for:", key)

    comparisons = 0
    found = False

    for i in range(len(arr)):
        comparisons += 1
        print("Comparison", comparisons, ":", arr[i], "with", key)

        if arr[i] == key:
            print("Element found at position", i + 1)
            found = True
            break

    if not found:
        print("Element not found")

    print("Total comparisons =", comparisons)


print("\nComplexity Analysis")
print("Best-case complexity = O(1)")
print("Average-case complexity = O(n)")
print("Worst-case complexity = O(n)")
print("Space complexity = O(1)")

text = "AABAACAADAABAABA"
pattern = "AABA"

positions = []
comparisons = 0

for i in range(len(text) - len(pattern) + 1):
    j = 0

    while j < len(pattern):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break

        j += 1

    if j == len(pattern):
        positions.append(i)

print("Pattern occurrences at positions:", positions)
print("Total number of comparisons =", comparisons)

text = "BANANABANANA"
pattern = "ANA"

positions = []

for i in range(len(text) - len(pattern) + 1):
    j = 0

    while j < len(pattern) and text[i + j] == pattern[j]:
        j += 1

    if j == len(pattern):
        positions.append(i)

print("Occurrences at positions:", positions)

text = "MISSISSIPPI"
pattern = "ISSI"

for shift in range(len(text) - len(pattern) + 1):
    comparisons = 0
    matched = True

    for j in range(len(pattern)):
        comparisons += 1

        if text[shift + j] != pattern[j]:
            matched = False
            break

    if matched:
        result = "Match"
    else:
        result = "Mismatch"

    print(
        "Shift:", shift,
        "| Comparisons:", comparisons,
        "| Result:", result
    )

text = "ABABABABAB"
pattern = "ABAB"

comparisons = 0
matches = 0
mismatches = 0

for i in range(len(text) - len(pattern) + 1):
    for j in range(len(pattern)):
        comparisons += 1

        if text[i + j] == pattern[j]:
            matches += 1
        else:
            mismatches += 1
            break

print("Total character comparisons =", comparisons)
print("Total matches =", matches)
print("Total mismatches =", mismatches)

text = "AAAAAAAAAB"
pattern = "AAAAB"

comparisons = 0
found = False

for i in range(len(text) - len(pattern) + 1):
    j = 0

    while j < len(pattern):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break

        j += 1

    if j == len(pattern):
        found = True
        break

if found:
    print("Pattern found")
else:
    print("Pattern not found")

print("Number of comparisons =", comparisons)

print("Case: Worst Case")

text = "COMPUTERSCIENCE"
pattern = "SCI"

comparisons = 0
position = -1

for i in range(len(text) - len(pattern) + 1):
    j = 0

    while j < len(pattern):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break

        j += 1

    if j == len(pattern):
        position = i
        break

if position != -1:
    print("First occurrence position =", position)
else:
    print("Pattern not found")

print("Number of comparisons =", comparisons)

text = "DataStructuresAndAlgorithms"
pattern = "ALGORITHMS"

text_lower = text.lower()
pattern_lower = pattern.lower()

position = -1

for i in range(len(text_lower) - len(pattern_lower) + 1):
    j = 0

    while j < len(pattern_lower):
        if text_lower[i + j] != pattern_lower[j]:
            break
        j += 1

    if j == len(pattern_lower):
        position = i
        break

if position != -1:
    print("Pattern found at position", position + 1)
else:
    print("Pattern not found")

def brute_force_search(text, pattern):
    comparisons = 0

    for i in range(len(text) - len(pattern) + 1):
        j = 0

        while j < len(pattern):
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == len(pattern):
            return i, comparisons

    return -1, comparisons


text = "PROGRAMMINGLAB"

position1, comparisons1 = brute_force_search(text, "LAB")
position2, comparisons2 = brute_force_search(text, "TEST")

print("Successful search:")
print("Position =", position1)
print("Comparisons =", comparisons1)

print("\nUnsuccessful search:")
print("Position =", position2)
print("Comparisons =", comparisons2)

text = "ABCDABCABCDA"
pattern = "ABCDA"

occurrences = []

for alignment in range(len(text) - len(pattern) + 1):
    matched = True

    for j in range(len(pattern)):
        if text[alignment + j] != pattern[j]:
            matched = False
            break

    if matched:
        occurrences.append(alignment)

    print(
        "Alignment number:", alignment,
        "| Matching result:", "Match" if matched else "Mismatch"
    )

print("Pattern occurrence positions:", occurrences)

text = "TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
pattern = "TATCTT"

occurrences = []
total_comparisons = 0

print("Shifting process:")

for shift in range(len(text) - len(pattern) + 1):
    j = 0
    comparisons = 0

    while j < len(pattern):
        comparisons += 1
        total_comparisons += 1

        print(
            "Shift", shift,
            ":", "Text =", text[shift + j],
            "Pattern =", pattern[j]
        )

        if text[shift + j] != pattern[j]:
            print("Mismatch")
            break

        print("Match")
        j += 1

    if j == len(pattern):
        occurrences.append(shift)
        print("Pattern found at position", shift)
    else:
        print("Shift to next position")

print("\nPattern occurrences:", occurrences)
print("Total comparisons =", total_comparisons)

print("\nComplexity Analysis")
print("Best-case complexity = O(n)")
print("Worst-case complexity = O(n × m)")
print("Space complexity = O(1)")

