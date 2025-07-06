import matplotlib.pyplot as plt
import numpy as np
from optimization.hill_climbing import hill_climbing
from optimization.random_local_search import random_local_search
from optimization.simulated_annealing import simulated_annealing

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def plot_result(solution, algo_name):
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2  # сфера

    plt.figure()
    cp = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(cp)
    plt.scatter(solution[0], solution[1], color='red', s=50, label='Best solution')
    plt.title(f'{algo_name} result')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'screenshots/{algo_name}_result.png')
    plt.close()

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Hill Climbing:\nРозв'язок:", hc_solution, "Значення:", hc_value)
    plot_result(hc_solution, 'hill_climbing')

    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("\nRandom Local Search:\nРозв'язок:", rls_solution, "Значення:", rls_value)
    plot_result(rls_solution, 'random_local_search')

    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("\nSimulated Annealing:\nРозв'язок:", sa_solution, "Значення:", sa_value)
    plot_result(sa_solution, 'simulated_annealing')
