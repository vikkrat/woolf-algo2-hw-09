import random
import math

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        if temp < epsilon:
            break
        neighbor = [xi + random.uniform(-0.5, 0.5) for xi in current]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)

        delta = neighbor_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_value = neighbor, neighbor_value

        temp *= cooling_rate

    return current, current_value
