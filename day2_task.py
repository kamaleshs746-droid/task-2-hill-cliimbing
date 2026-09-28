import heapq

# ============================================================
# PART 1: A* SEARCH
# ============================================================

graph = {
    'S': {'A': 3, 'C': 2},
    'A': {'B': 4},
    'B': {'D': 5},
    'C': {'D': 2},
    'D': {}
}

heuristic = {
    'S': 4,
    'A': 7,
    'B': 5,
    'C': 2,
    'D': 0
}


def a_star(start, goal):
    open_list = [(heuristic[start], start)]

    g_cost = {start: 0}
    parent = {start: None}
    explored = []

    while open_list:

        f, current = heapq.heappop(open_list)

        # Ignore outdated entries
        if f != g_cost[current] + heuristic[current]:
            continue

        explored.append(current)

        g = g_cost[current]
        h = heuristic[current]

        print(f"Node: {current} | g = {g} | h = {h} | f = {g + h}")

        if current == goal:
            break

        for neighbor, cost in graph[current].items():

            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, neighbor)
                )

    # Create final path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, g_cost[goal], explored


print("=" * 50)
print("PART 1 - A* SEARCH")
print("=" * 50)

path, cost, explored = a_star('S', 'D')

print("\nNodes Explored:")
print(" -> ".join(explored))

print("\nFinal Path:")
print(" -> ".join(path))

print("\nTotal Cost:")
print(cost)


# ============================================================
# PART 2: HILL CLIMBING
# ============================================================

def function(x):
    return (x - 5) ** 2 + 10


def hill_climbing(start_x, step=1):

    current_x = start_x

    print("\n" + "=" * 50)
    print("PART 2 - HILL CLIMBING")
    print("=" * 50)

    while True:

        current_value = function(current_x)

        print(
            f"x = {current_x}, "
            f"f(x) = {current_value}"
        )

        # Generate neighbors
        left_x = current_x - step
        right_x = current_x + step

        left_value = function(left_x)
        right_value = function(right_x)

        # Move to better neighbor
        if left_value < current_value and left_value <= right_value:

            current_x = left_x

        elif right_value < current_value:

            current_x = right_x

        else:
            break

    return current_x, function(current_x)


# Starting value
initial_x = 0

best_x, minimum = hill_climbing(initial_x)

print("\nFinal Result:")
print(f"Minimum x = {best_x}")
print(f"Minimum f(x) = {minimum}")