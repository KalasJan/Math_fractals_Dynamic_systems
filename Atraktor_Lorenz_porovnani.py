# lorenzuv atraktor - porovnani rozdilu parametru

import matplotlib.pyplot as plt
import numpy as num

# parametry (nejcasteji S = 10, R = 28, B = 8/3)
sigma1 = "10"
sigma2 = "10.12"
ro1 = "28"
ro2 = "15"
beta1 = "8/3"
beta2 = "5/4"

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


# kresleni
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection="3d")

# obe linie vedle sebe
ax.plot(*podm1.T, lw=0.4, color="royalblue", label=fr"$\sigma$ = {sigma1}, $\rho$ = {ro1}, $\beta$ = {beta1}")
ax.plot(*podm2.T, lw=0.4, color="crimson", label=fr"$\sigma$ = {sigma2}, $\rho$ = {ro2}, $\beta$ = {beta2}")

# Pocatecni bod
ax.scatter([0], [1], [1.05], color="black", s=50, zorder=5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenzův atraktor – Ukázka chaosu (Porovnání různých počátečních podmínek)", weight="bold")

ax.legend()


plt.show()