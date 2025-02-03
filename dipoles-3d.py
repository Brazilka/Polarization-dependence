# final version 29/01/2025
import numpy as np
import matplotlib.pyplot as plt

# Define theta
theta = np.pi / 2
phi = np.pi / 2 # "detector"
e_i = np.array([np.cos(theta), np.sin(theta), 0]) # amplitude of electric field vector, incident light polarized along xz plane
e_s = np.array([np.cos(phi), np.sin(phi), 0]) 

# Define Raman tensors for B1 and B2 modes
d=1
c=1
R_B2 = np.array([[0, d, 0],
                 [d, 0, 0],
                 [0, 0, 0]])
R_B1 = np.array([[c, 0, 0], 
                 [0, -c, 0],
                 [0, 0, 0]])

# induced dipole moment mi = alpha . E, doesnt depend on e_s
dipole_B1 = np.dot(R_B1, e_i)
dipole_B2 = np.dot(R_B2, e_i)
# calculate intensity, depends on e_s
#  I as |e_s^T * R * e_i|**2
print("Intensity of R_B1 is:")
intensity_B1 = abs(np.matmul(e_s.transpose(),dipole_B1))**2
print(intensity_B1)
print("Intensity of R_B2 is:")
intensity_B2 = abs(np.matmul(e_s.transpose(),dipole_B2))**2
print(intensity_B2)


# set up 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, e_i[0], e_i[1], e_i[2], color='green', label=r"$\mathbf{e}_{i}$",linewidth=3)
ax.scatter(e_i[0], e_i[1], e_i[2], color='green', s=50) # green like incident laser
ax.quiver(0, 0, 0, dipole_B1[0], dipole_B1[1], dipole_B1[2], color='red', label=r"$\mathbf{\mu} \, (B_1)$", linewidth=3)
ax.quiver(0, 0, 0, dipole_B2[0], dipole_B2[1], dipole_B2[2], color='blue', label=r"$\mathbf{\mu} \, (B_2)$", linewidth=3)

# set plot limits, labels, and legend
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r"$\theta_{i} = 90°$" , fontsize=20)
ax.legend(fontsize=15)
ax.grid()

plt.show()