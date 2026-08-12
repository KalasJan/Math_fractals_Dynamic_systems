# lorenzuv atraktor - porovnani rozdilu parametru

import matplotlib.animation as animace
import matplotlib.pyplot as plt
import numpy as num

# parametry (nejcasteji S = 10, R = 28, B = 8/3)
sigma1 = "10"
sigma2 = "10.12"
ro1 = "28"
ro2 = "28.01"
beta1 = "8/3"
beta2 = "8/3"

# pokud by parametr byl zlomek
s1_num = float(eval(str(sigma1)))
s2_num = float(eval(str(sigma2)))
r1_num = float(eval(str(ro1)))
r2_num = float(eval(str(ro2)))
b1_num = float(eval(str(beta1)))
b2_num = float(eval(str(beta2)))

# definice systemu ODE
def lorenz(xyz, *, sigma, ro, beta):
    x, y, z = xyz
    dx = sigma*(y - x)
    dy = x * (ro - z) - y
    dz = x*y - beta*z
    return num.array([dx, dy, dz])

dt = 0.01 # delka casoveho kroku
kroku = 3000 # pocet kroku

#system1
podm1 = num.empty((kroku + 1, 3))  # vice pocatecnich podminek
podm1[0] = (0, 1, 1.05)  # nastaveni podminek v case 0
for p in range(kroku):
    podm1[p + 1] = podm1[p] + lorenz(podm1[p], sigma=s1_num, ro=r1_num, beta=b1_num) * dt

# system2
podm2 = num.empty((kroku + 1, 3))  # vice pocatecnich podminek
podm2[0] = (0, 1, 1.05)  # nastaveni podminek v case 0
for p in range(kroku):
    podm2[p + 1] = podm2[p] + lorenz(podm2[p], sigma=s2_num, ro=r2_num, beta=b2_num) * dt

# video

fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(projection='3d')

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_zlim(0, 50)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Porovnání Lorenzových atraktorů - vizualizace chaosu")

# prazdne objekty pro caru a dany bod
(line1,) = ax.plot([], [], [], lw=0.6, color="royalblue")
(point1,) = ax.plot([], [], [], "o", color="blue", ms=5)

(line2,) = ax.plot([], [], [], lw=0.6, color="crimson")
(point2,) = ax.plot([], [], [], "o", color="red", ms=5)


# funkce pro video (kazdy snimek)
def aktualizace(snimek): # od zactku po aktualni
    # system 1 (modry)
    line1.set_data(podm1[:snimek, 0], podm1[:snimek, 1])
    line1.set_3d_properties(podm1[:snimek, 2])
    if snimek > 0:
        point1.set_data([podm1[snimek - 1, 0]], [podm1[snimek - 1, 1]])
        point1.set_3d_properties([podm1[snimek - 1, 2]])
    
    # system 2 (cerveny)
    line2.set_data(podm2[:snimek, 0], podm2[:snimek, 1])
    line2.set_3d_properties(podm2[:snimek, 2])
    if snimek > 0:
        point2.set_data([podm2[snimek - 1, 0]], [podm2[snimek - 1, 1]])
        point2.set_3d_properties([podm2[snimek - 1, 2]])
    
    # rotace zobrazeni
    ax.view_init(elev=20, azim=0.2 * snimek)

    return line1, point1, line2, point2

# spusteni animace

line1.set_label(fr"$\sigma = {sigma1}, \rho = {ro1}, \beta = {beta1}$")
line2.set_label(fr"$\sigma = {sigma2}, \rho = {ro2}, \beta = {beta2}$")
ax.legend()

animation = animace.FuncAnimation(
    fig,
    aktualizace,
    frames=range(1, kroku + 1, 5),
    interval=10,
    blit=False,
    repeat=False,
)

plt.show()