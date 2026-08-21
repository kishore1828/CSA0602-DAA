import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(points):
    min_distance = float("inf")
    closest = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])

            if d < min_distance:
                min_distance = d
                closest = (points[i], points[j])

    return closest, min_distance


points = [(1, 2), (4, 5), (7, 8), (3, 1)]

pair, min_dist = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", min_dist)

import math


def euclidean_distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def closest_pair(points):
    minimum = float("inf")
    pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = euclidean_distance(points[i], points[j])

            if d < minimum:
                minimum = d
                pair = (points[i], points[j])

    return pair, minimum


points = [(2, 3), (5, 4), (1, 7), (8, 9), (4, 6)]

pair, minimum = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", minimum)

import math


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def closest_pair(points):
    min_distance = float("inf")
    closest = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            current_distance = distance(points[i], points[j])

            if current_distance < min_distance:
                min_distance = current_distance
                closest = (points[i], points[j])

    return closest, min_distance


points = [(0, 0), (2, 2), (3, 1), (6, 5)]

pair, minimum = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", minimum)

import math


def calculate_distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def closest_pair(points):
    minimum_distance = float("inf")
    closest = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = calculate_distance(points[i], points[j])

            if d < minimum_distance:
                minimum_distance = d
                closest = (points[i], points[j])

    return closest, minimum_distance


points = [(10, 20), (15, 25), (30, 40), (12, 22)]

pair, minimum = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", minimum)

import math


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def closest_pair(points):
    minimum = float("inf")
    pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])

            if d < minimum:
                minimum = d
                pair = (points[i], points[j])

    return pair, minimum


def orientation(a, b, c):
    value = (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0


def convex_hull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            left = False
            right = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                value = orientation(points[i], points[j], points[k])

                if value > 0:
                    left = True
                elif value < 0:
                    right = True

            if not (left and right):
                if points[i] not in hull:
                    hull.append(points[i])

                if points[j] not in hull:
                    hull.append(points[j])

    # Arrange hull points around the polygon
    center_x = sum(p[0] for p in hull) / len(hull)
    center_y = sum(p[1] for p in hull) / len(hull)

    hull.sort(
        key=lambda p: math.atan2(
            p[1] - center_y,
            p[0] - center_x
        )
    )

    return hull


points = [
    (10, 0),
    (11, 5),
    (5, 3),
    (9, 3.5),
    (15, 3),
    (12.5, 7),
    (6, 6.5),
    (7.5, 4.5)
]

pair, minimum = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", minimum)

hull = convex_hull(points)

print("\nConvex Hull:")
for point in hull:
    print(point)

print("\nTime Complexity for Closest Pair: O(n^2)")
print("Time Complexity for Brute Force Convex Hull: O(n^3)")
print("Space Complexity: O(n)")
print("For multiple collinear points, orientation = 0 is handled as a boundary case.")

def orientation(a, b, c):
    value = (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def convex_hull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            positive = False
            negative = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                value = orientation(points[i], points[j], points[k])

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

            if not (positive and negative):
                if points[i] not in hull:
                    hull.append(points[i])

                if points[j] not in hull:
                    hull.append(points[j])

    # Start from the lowest point and arrange counter-clockwise
    start = min(hull, key=lambda p: (p[1], p[0]))

    def cross_angle(p):
        import math
        return math.atan2(
            p[1] - start[1],
            p[0] - start[0]
        )

    hull.remove(start)
    hull.sort(key=cross_angle)
    hull.insert(0, start)

    return hull


points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]

hull = convex_hull(points)

print("Convex Hull Points:")
for point in hull:
    print(point)

def orientation(a, b, c):
    value = (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0


def convex_hull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            positive = False
            negative = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                value = orientation(points[i], points[j], points[k])

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

            if not (positive and negative):
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull


points = [
    (1, 2),
    (3, 1),
    (5, 3),
    (4, 6),
    (2, 5)
]

hull = convex_hull(points)

print("Convex Hull Points:")
for point in hull:
    print(point)

def orientation(a, b, c):
    value = (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0


def convex_hull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            positive = False
            negative = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                value = orientation(points[i], points[j], points[k])

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

            if not (positive and negative):
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    # Arrange points around the boundary
    center_x = sum(p[0] for p in hull) / len(hull)
    center_y = sum(p[1] for p in hull) / len(hull)

    import math

    hull.sort(
        key=lambda p: math.atan2(
            p[1] - center_y,
            p[0] - center_x
        )
    )

    return hull


points = [(0, 3), (1, 1), (2, 2), (4, 4), (3, 0)]

hull = convex_hull(points)

print("Convex Hull Points:")
for point in hull:
    print(point)

def orientation(a, b, c):
    value = (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0


def convex_hull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            positive = False
            negative = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                value = orientation(points[i], points[j], points[k])

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

            if not (positive and negative):
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull


points = [
    (2, 2),
    (4, 1),
    (6, 3),
    (5, 5),
    (3, 6),
    (1, 4)
]

hull = convex_hull(points)

print("Convex Hull Points:")
for point in hull:
    print(point)

def orientation(a, b, c):
    value = (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0


def convex_hull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            positive = False
            negative = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                value = orientation(points[i], points[j], points[k])

                if value > 0:
                    positive = True
                elif value < 0:
                    negative = True

            if not (positive and negative):
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull


points = [
    (1, 1),
    (2, 4),
    (5, 5),
    (6, 2),
    (3, 0)
]

hull = convex_hull(points)

print("Convex Hull Points:")
for point in hull:
    print(point)

def subset_sum(numbers, target):
    n = len(numbers)

    for mask in range(1, 1 << n):
        subset = []
        total = 0

        for i in range(n):
            if mask & (1 << i):
                subset.append(numbers[i])
                total += numbers[i]

        if total == target:
            return subset

    return None


numbers = [3, 34, 4, 12, 5, 2]
target = 9

result = subset_sum(numbers, target)

if result:
    print("Subset found:", result)
    print("Sum:", sum(result))
else:
    print("No subset found")

import math


def distance(a, b):
    return math.sqrt(
        (a[0] - b[0]) ** 2 +
        (a[1] - b[1]) ** 2
    )


def total_path_distance(path):
    total = 0

    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1])

    return total


def shortest_path(cities):
    from itertools import permutations

    start = cities[0]
    remaining = cities[1:]

    best_distance = float("inf")
    best_path = None

    for perm in permutations(remaining):
        path = [start] + list(perm) + [start]
        current_distance = total_path_distance(path)

        if current_distance < best_distance:
            best_distance = current_distance
            best_path = path

    return best_path, best_distance


test_cases = [
    [(1, 2), (4, 5), (7, 1), (3, 6)],
    [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
]

for number, cities in enumerate(test_cases, start=1):
    path, shortest = shortest_path(cities)

    print("Test Case", number)
    print("Shortest Distance:", shortest)
    print("Shortest Path:", path)
    print()

from itertools import permutations


def total_cost(assignment, cost_matrix):
    total = 0

    for worker, task in enumerate(assignment):
        total += cost_matrix[worker][task]

    return total


def assignment_problem(cost_matrix):
    n = len(cost_matrix)

    best_assignment = None
    minimum_cost = float("inf")

    for assignment in permutations(range(n)):
        current_cost = total_cost(assignment, cost_matrix)

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_assignment = assignment

    return best_assignment, minimum_cost


test_cases = [
    [
        [3, 10, 7],
        [8, 5, 12],
        [4, 6, 9]
    ],
    [
        [15, 9, 4],
        [8, 7, 18],
        [6, 12, 11]
    ]
]


for number, cost_matrix in enumerate(test_cases, start=1):
    assignment, cost = assignment_problem(cost_matrix)

    print("Test Case", number)
    print("Optimal Assignment:")

    for worker in range(len(assignment)):
        print(
            "(worker", worker + 1,
            ", task", assignment[worker] + 1,
            ")"
        )

    print("Total Cost:", cost)
    print()

def total_value(items, values):
    total = 0

    for index in items:
        total += values[index]

    return total


def is_feasible(items, weights, capacity):
    total_weight = 0

    for index in items:
        total_weight += weights[index]

    return total_weight <= capacity


def knapsack_exhaustive(weights, values, capacity):
    n = len(weights)

    best_items = []
    best_value = 0

    for mask in range(1 << n):
        selected = []

        for i in range(n):
            if mask & (1 << i):
                selected.append(i)

        if is_feasible(selected, weights, capacity):
            value = total_value(selected, values)

            if value > best_value:
                best_value = value
                best_items = selected

    return best_items, best_value


test_cases = [
    ([2, 3, 1], [4, 5, 3], 4),
    ([1, 2, 3, 4], [2, 4, 6, 3], 6)
]


for number, (weights, values, capacity) in enumerate(test_cases, start=1):
    selected, value = knapsack_exhaustive(
        weights,
        values,
        capacity
    )

    print("Test Case", number)
    print("Optimal Selection:", selected)
    print("Total Value:", value)
    print()

def find_subset(numbers, target):
    n = len(numbers)

    for mask in range(1, 1 << n):
        subset = []
        total = 0

        for i in range(n):
            if mask & (1 << i):
                subset.append(numbers[i])
                total += numbers[i]

        if total == target:
            return subset

    return None


numbers = [15, 10, 12, 7, 5]
target = 22

result = find_subset(numbers, target)

if result:
    print("Subset found:", result)
    print("Sum:", sum(result))
else:
    print("No subset found")
