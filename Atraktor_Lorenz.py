# lorenzuv atraktor

import matplotlib.pyplot as mal
import numpy as num

# parametry (nejcasteji S = 10, R = 28, B = 8/3)
sigma = 10
ro = 28
beta = 8/3

# definice systemu ODE
def lorenz(xyz, *, sigma, ro, beta):
    x, y, z = xyz
    dx = sigma*(y - x)
    dy = x * (ro-z) - y
    dz = x*y - beta*z
    return num.array([dx, dy, dz])

dt = 0.1 # delka casoveho kroku
kroku = 1000 # pocet kroku

podm = num.empty((kroku + 1, 3))  # vice pocatecnich podminek
podm[0] = (0, 1, 1.05)  # nastaveni podminek v case 0
for p in range(kroku):
    podm[p + 1] = podm[p] + lorenz(podm[p], sigma=sigma, ro=ro, beta=beta) * dt

# kresleni
ax = mal.figure().add_subplot(projection='3d')

ax.plot(*podm.T, lw=0.35)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# ax.set_title("Lorenzuv atraktor")
mal.axis('off') # bez os

mal.show()