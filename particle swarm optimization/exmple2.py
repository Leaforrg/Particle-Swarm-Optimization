import random

# The function we want to minimize (Parabola)
def fitness_function(position):
    return sum(p**2 for p in position)

# Particle properties
num_particles = 15
dim = 2
w, c1, c2 = 0.5, 1.5, 1.5  # Hyperparameters

# Initialize positions, velocities, and "personal bests"
particles = [[random.uniform(-10, 10) for _ in range(dim)] for _ in range(num_particles)]
velocities = [[0 for _ in range(dim)] for _ in range(num_particles)]
pbest = list(particles)
gbest = min(pbest, key=fitness_function)

for _ in range(100):
    for i in range(num_particles):
        for d in range(dim):
            # Update Velocity: inertia + cognitive + social
            r1, r2 = random.random(), random.random()
            velocities[i][d] = (w * velocities[i][d] + 
                                c1 * r1 * (pbest[i][d] - particles[i][d]) + 
                                c2 * r2 * (gbest[d] - particles[i][d]))
            # Update Position
            particles[i][d] += velocities[i][d]
            
        # Update Bests
        if fitness_function(particles[i]) < fitness_function(pbest[i]):
            pbest[i] = list(particles[i])
        if fitness_function(pbest[i]) < fitness_function(gbest):
            gbest = list(pbest[i])

print(f"Global Best Position: {gbest}")