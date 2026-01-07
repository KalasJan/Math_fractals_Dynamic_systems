#vykresli Rossleruv atraktor

import matplotlib.pyplot as mal
import numpy as num

# parametry
a = 0.21
b = 0.21
c = 5.71

# definice systemu ODE
def ross(xyz, *, a, b, c):
    x, y, z = xyz
    dx = - y - z
    dy = x + a * y
    dz = b +z * (x - c)
    return num.array([dx, dy, dz])

dt = 0.01 # delka casoveho kroku
kroku = 100000 # pocet kroku

podm = num.empty((kroku + 1, 3))  # vice pocatecnich podminek
podm[0] = (0, 1, 1.05)  # nastaveni podminek v case 0
for p in range(kroku):
    podm[p + 1] = podm[p] + ross(podm[p], a=a, b=b, c=c) * dt

# kresleni
ax = mal.figure().add_subplot(projection='3d')

ax.plot(*podm.T, lw=0.5, color = 'black')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Rossleruv atraktor")
mal.axis('off') # bez os

mal.show()