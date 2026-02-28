import matplotlib.pyplot as plt
import numpy as np

# 1. Setup our "World" constants
gravity = 9.81        # Earth's gravity in m/s^2
initial_velocity = 30 # How fast we throw the ball (meters per second)
time_total = 6.2      # Total seconds to track

# 2. Create a list of time points (from 0 to 6.2 seconds)
# This creates 100 tiny steps so the movement looks smooth
time_steps = np.linspace(0, time_total, 100)

# 3. The Physics Simulation (The Math)
# Calculate the height for every single time step
heights = (initial_velocity * time_steps) - (0.5 * gravity * time_steps**2)

# 4. Visualization (Drawing the graph)
plt.figure(figsize=(8, 5))
plt.plot(time_steps, heights, color='blue', linewidth=2)
plt.title("Physics Simulation: Projectile Motion")
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.grid(True)
plt.show()
