import random

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value - epsilon:
            best, best_value = candidate, candidate_value

    return best, best_value
