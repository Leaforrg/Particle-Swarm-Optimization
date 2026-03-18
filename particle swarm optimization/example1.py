import pyswarms as ps
import numpy as np

# Define the Sphere function
def sphere_func(x):
    return np.sum(x**2, axis=1)

# Set hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

# Call instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)

# Perform optimization
best_cost, best_pos = optimizer.optimize(sphere_func, iters=100)

print(f"Best Position: {best_pos}")