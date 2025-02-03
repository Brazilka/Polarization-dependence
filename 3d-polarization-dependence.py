# final version 29/01/2025
import numpy as np
import matplotlib.pyplot as plt
theta = np.radians(np.arange(0, 181, 10))  # radians
phi = np.radians(0)   # fixed "detector" angle

# Raman tensors
a = 1
b = 1
R_A1 = np.array([[a, 0, 0],
                 [0, a, 0],
                 [0, 0, a]])

R_B2 = np.array([[0, b, 0],
                 [b, 0, 0],
                 [0, 0, 0]])

# set up 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# loop through theta
for idx_t,t in enumerate(theta):
    e_i = np.array([np.sin(t), np.cos(t), 0])
    e_s = np.array([np.sin(phi), np.cos(phi), 0])
# calculate scattered electric field vectors
    dipole_B2 = np.matmul(R_B2, e_i)
    dipole_A1 = np.matmul(R_A1, e_i)

# clear the plot for the current angle
    ax.clear()
# plot Ein
    ax.quiver(0, 0, 0, e_i[0], e_i[1], e_i[2], color='green', label=r"$\mathbf{e}_{i}$", linewidth=3)
# plot a point at the end of Ein for better visibility
    ax.scatter(e_i[0], e_i[1], e_i[2], color='green', s=50) # green like incident laser
# plot dipole vector for the B2 mode
    ax.quiver(0, 0, 0, dipole_B2[0], dipole_B2[1], dipole_B2[2], color='blue', label=r"$\mathbf{dipole}_{B_2}$", linewidth=3)
# plot dipoole for A1
    ax.quiver(0, 0, 0, dipole_A1[0], dipole_A1[1], dipole_A1[2], color='red', label=r"$\mathbf{dipole}_{A_1}$", linewidth=3)

# ensure plot limits are symmetric and large enough
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])
    # labels, legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(rf"$\theta = {np.degrees(t):.1f}^\circ$", fontsize=20)
    ax.legend(fontsize=12, loc="upper left", handlelength=2.5)
    ax.grid()
    # pause for visualization
    plt.pause(0.01)
plt.show()

  


