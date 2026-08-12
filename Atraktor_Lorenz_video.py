# lorenzuv atraktor - video

import matplotlib.pyplot as plt
import matplotlib.animation as animace
import numpy as num

# parametry (nejcasteji S = 10, R = 28, B = 8/3)
sigma = 10.12
ro = 28
beta = 8/3

# definice systemu ODE
def lorenz(xyz, *, sigma, ro, beta):
    x, y, z = xyz
    dx = sigma*(y - x)
    dy = x * (ro-z) - y
    dz = x*y - beta*z
    return num.array([dx, dy, dz])

dt = 0.01 # delka casoveho kroku
kroku = 3000 # pocet kroku

podm = num.empty((kroku + 1, 3))  # vice pocatecnich podminek
podm[0] = (0, 1, 1.05)  # nastaveni podminek v case 0
for p in range(kroku):
    podm[p + 1] = podm[p] + lorenz(podm[p], sigma=sigma, ro=ro, beta=beta) * dt

# kresleni
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_zlim(0, 50)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenzuv atraktor")

# prazdne objekty pro caru a dany bod
(line,) = ax.plot([], [], [], lw=0.6, color="royalblue")
(point,) = ax.plot([], [], [], "o", color="crimson", ms=6)

# funkce pro video (kazdy snimek)
def aktualizace(snimek): # od zactku po aktualni
    data_x = podm[:snimek, 0]
    data_y = podm[:snimek, 1]
    data_z = podm[:snimek, 2]
    
    # Aktualizace vykreslenou čáru
    line.set_data(data_x, data_y)
    line.set_3d_properties(data_z)
    
    # pokud mame 1 bo, udelame cerveny bod na konci (ve smeru)
    if snimek > 0:
        point.set_data([podm[snimek - 1, 0]], [podm[snimek - 1, 1]])
        point.set_3d_properties([podm[snimek - 1, 2]])
    
    # rotace zobrazeni
    ax.view_init(elev=20, azim=0.3 * snimek)

    return line, point

# spusteni animace
animation = animace.FuncAnimation(
    fig,
    aktualizace,
    frames=range(1, kroku + 1, 5),
    interval=10,
    blit=False,
    repeat=False,
)

plt.show()