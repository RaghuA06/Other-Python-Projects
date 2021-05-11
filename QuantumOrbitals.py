from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def prob_1s(x, y, z):
    r = np.sqrt(np.square(x) + np.square(y) + np.square(z))
    return np.square(np.exp(-r) / np.sqrt(np.pi))

x = np.linspace(0, 1, 30)
y = np.linspace(0, 1, 30)
z = np.linspace(0, 1, 30)

elements = []
probability = []

for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix, iy, iz)))
            probability.append(prob_1s(ix, iy, iz))

probability = probability / sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05, s=2)
ax.set_title("Hydrogen 1s density")
plt.show()
