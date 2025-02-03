# final version 29/01/2025
### definitions from https://doi.org/10.1038/s41467-019-13504-8, supplementary ###
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# theta and phi in degrees, convert to radians
theta_deg = np.linspace(0, 360, 360) # incident light
theta = np.radians(theta_deg)
phi_deg = np.linspace(0, 360, 360) # scattered light (angle of "detector")
phi = np.radians(phi_deg)

# create 2d grid, define tensor
theta_grid, phi_grid = np.meshgrid(theta, phi)
b = 1
R = np.array([[b, 0, 0],
              [0, b, 0],
              [0, 0, b]])

dot_product_values = np.zeros_like(theta_grid)
cross_product_values = np.zeros_like(theta_grid)
intensity_list = []

# intensity, dot and cross product
for i in range(theta_grid.shape[0]):
    for j in range(theta_grid.shape[1]):
        theta_val = theta_grid[i, j]
        phi_val = phi_grid[i, j]
        e_i = np.array([np.sin(theta_val), np.cos(theta_val), 0])
        e_s = np.array([np.sin(phi_val), np.cos(phi_val), 0])
        dot_product_values[i, j] = np.abs(np.dot(e_i, e_s)) # result of dot is a scalar with a sign, here I want absolute value
        cross_product_values[i, j] = np.linalg.norm(np.cross(e_i, e_s)) # result of cross is a vector
        # scattering intensity  as |e_s^T * R * e_i|**2
        intermediate = np.matmul(e_i.transpose(),R)
        electric_field = np.matmul(intermediate, e_s)
        intensity_list.append(np.abs(electric_field)**2)

intensity_list = np.array(intensity_list).reshape(theta_grid.shape)

# Find where the dot product is zero (orthogonal vectors)
dot_zero = np.isclose(dot_product_values, 0, atol=1e-10)
dot_zero_indices = np.where(dot_zero)
dot_zero_intensities = intensity_list[dot_zero_indices]

# orthogonal vectors and their intensity
print("Intensity for orthogonal vectors:")
for i in range(len(dot_zero_indices[0])):
    theta_val = np.degrees(theta_grid[dot_zero_indices[0][i], dot_zero_indices[1][i]])
    phi_val = np.degrees(phi_grid[dot_zero_indices[0][i], dot_zero_indices[1][i]])
    intensity = dot_zero_intensities[i]
    print(f"Theta: {theta_val:.2f}, Phi: {phi_val:.2f}, Intensity: {intensity:.4f}")

# plot dot product (2D)
plt.figure(figsize=(10, 8))
plt.imshow(dot_product_values, extent=[0, 360, 0, 360], origin='lower', aspect='auto', cmap='plasma')
plt.colorbar(label='Absolute value')
plt.title('Dot product of $\mathbf{e}_i$ and $\mathbf{e}_s$, 0 = orthogonal.', fontsize=16)
plt.xlabel(r'$\theta_{i}$ (°)', fontsize=15)
plt.ylabel(r'$\phi_{s}$ (°)', fontsize=15)
plt.grid(False)
plt.show()

# plot cross product magnitude (2D)
plt.figure(figsize=(10, 8))
plt.imshow(cross_product_values, extent=[0, 360, 0, 360], origin='lower', aspect='auto', cmap='plasma')
plt.colorbar(label='Magnitude')
plt.title('Cross product of $\mathbf{e}_i$ and $\mathbf{e}_s$, 0 = parallel.', fontsize=16)
plt.xlabel(r'$\theta_{i}$ (°)', fontsize=15)
plt.ylabel(r'$\phi_{s}$ (°)', fontsize=15)
plt.grid(False)
plt.show()

# plot scattered intensity (2D)
plt.figure(figsize=(10, 8))
plt.imshow(intensity_list, extent=[0, 360, 0, 360], origin='lower', aspect='auto', cmap='viridis')
plt.colorbar(label='Intensity (a.u.)')
plt.title(r'Scattered intensity of $\mathbf{A_1}$ for all $\theta_{i}$ and $\phi_{s}$ combinations', fontsize=16)
plt.xlabel(r'$\theta_{i}$ (°)', fontsize=15)
plt.ylabel(r'$\phi_{s}$ (°)', fontsize=15)
plt.grid(False)
plt.show()


