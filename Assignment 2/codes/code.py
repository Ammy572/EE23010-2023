import matplotlib.pyplot as plt
import numpy as np

# Circle parameters
center = np.array([0, 0])
point_A = np.array([1, -1])
radius = np.linalg.norm(point_A - center)

# Create an array of angles
theta = np.linspace(0, 2*np.pi, 100)

# Calculate the coordinates of the circle points
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# Plot the circle
plt.figure(figsize=(6, 6))
plt.plot(x, y, label=f'Circle: Center O(0,0), Radius R={radius:.2f}')
plt.plot(center[0], center[1], 'go', label='Center O(0,0)')
plt.plot(point_A[0], point_A[1], 'ro', label='Point A(1,-1)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend(loc='best')
plt.axis('equal')  # Equal aspect ratio ensures the circle looks round
plt.show()
