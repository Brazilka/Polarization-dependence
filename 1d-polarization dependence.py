# final version 29/01/2025
### definitions from https://doi.org/10.1038/s41467-019-13504-8, ###
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 360)  # in radians, 0 to 360
phi = np.radians(90) # detected along x-axis, see definition of e_s
a = 1
b = 2

R_B2 = np.array([[0, b, 0],
                 [b, 0, 0],
                 [0, 0, 0]])
R_A1 = np.array([[a, 0, 0],
                 [0, a, 0],
                 [0, 0, a]])

# assume e_i is polarized along x
# intensity as |e_s^T * R_B2 * e_i|**2
intensity_B2 = []
intensity_A1 = []
#B2
for t in theta:
  e_i = np.array([np.cos(t), np.sin(t), 0]) # LP light 
  e_s = np.array([np.cos(phi), np.sin(phi), 0]) # detected along x-axis (phi=90)
    #  I as |e_s^T * R * e_i|**2
  intermediate = np.matmul(R_B2,e_i)
  electric_field = np.matmul(e_s.T, intermediate)
  intensity_B2.append(np.abs(electric_field)**2)
#A1
for t in theta:
  e_i = np.array([np.cos(t), np.sin(t), 0]) # LP light
  e_s = np.array([np.cos(phi), np.sin(phi), 0]) # detected along x-axis (phi=90)
  #  I as |e_s^T * R * e_i|**2
  intermediate = np.matmul(R_A1,e_i)
  electric_field = np.matmul(e_s.T, intermediate)
  intensity_A1.append(np.abs(electric_field)**2)

intensity_B2 = np.array(intensity_B2)
intensity_A1 = np.array(intensity_A1)

plt.figure(figsize=(10, 7))
plt.plot(np.degrees(theta), intensity_B2, label = r'$\mathit{B}_2$', color='blue', linewidth = 3)
plt.plot(np.degrees(theta), intensity_A1, label = r'$\mathit{A}_1$', color='red', linewidth = 3)
plt.title('Intensity detected along x-axis as a function of $\mathit{θ}_i$' , fontsize=16)
plt.xlabel('$\mathit{θ}_i$ (°)', fontsize=15)
plt.ylabel('Intensity (a.u.)', fontsize=15)
plt.grid(True)
plt.legend(fontsize=15)
plt.show()
