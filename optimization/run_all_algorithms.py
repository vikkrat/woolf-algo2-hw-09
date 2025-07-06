from hill_climbing import hill_climbing
from random_local_search import random_local_search
from simulated_annealing import simulated_annealing

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Hill Climbing:")
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("\nRandom Local Search:")
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("\nSimulated Annealing:")
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
