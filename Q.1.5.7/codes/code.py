import matplotlib.pyplot as plt
import numpy as np

# Coordinates of the center I
center = (-1.45, -0.78)

# Radius of the circle
radius = 1.896

# Coordinates of points A, B, and C
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])
# Generate theta values for creating points on the circle
theta = np.linspace(0, 2*np.pi, 100)

# Calculate the x and y coordinates of points on the circle
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the circle
ax.plot(x_circle, y_circle, label='Circle with center I and radius r')

# Mark the center I
ax.plot(center[0], center[1], marker='o', color='red', label='Center I')

# Plot points A, B, and C
ax.plot(A[0], A[1], marker='o', color='blue', label='Point A')
ax.plot(B[0], B[1], marker='o', color='green', label='Point B')
ax.plot(C[0], C[1], marker='o', color='purple', label='Point C')

# Connect the points A, B, and C with lines
ax.plot([A[0], B[0]], [A[1], B[1]], color='blue')
ax.plot([B[0], C[0]], [B[1], C[1]], color='green')
ax.plot([C[0], A[0]], [C[1], A[1]], color='purple')

# Plot the radius line from center to a point on the circle's circumference
ax.plot([center[0], center[0] + radius], [center[1], center[1]], color='black', label='Radius r')
# Set equal aspect ratio to make sure the circle is circular
ax.set_aspect('equal', adjustable='datalim')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Show the plot
plt.grid()
plt.show()

