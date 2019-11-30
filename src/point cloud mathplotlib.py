import numpy as np
# from ransac import *
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


fig = plt.figure()
ax = mplot3d.Axes3D(fig)

f = open('table_scene.pcd', 'r')
l = f.readlines()

xs = []
ys = []
zs = []

for point in l[11:451420:200]:
    x, y, z = [float(i) for i in point.split()]
    xs.append(x)
    ys.append(y)
    zs.append(z)

ax.scatter3D(xs, ys, zs)
plt.show()
