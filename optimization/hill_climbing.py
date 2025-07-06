import random

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        neighbor = [xi + random.uniform(-0.1, 0.1) for xi in current]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)

        if abs(current_value - neighbor_value) < epsilon:
            break

        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value

    return current, current_value
