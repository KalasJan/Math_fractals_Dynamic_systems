# Vykresli fazovy portret modelu Korist - dravec (Lotka - Voltera)
# bez vnitrodruhove konkurence i s ni

import numpy as np
import matplotlib.pyplot as plt

# koeficienty (vsechny musi byt vetsi nez 0)

a1 = 3.9 # plodnost koristi
a2 = a4 = 1 # interakce mezi koristi a dravci
a3 = 2 # umrtnost dravcu
b1 = b2 = 0.1 # vnitrodruhova konkurence

# ====================================================

def mezidruh(x,y):
    dx = a1 * x - a2 * x * y
    dy = - a3 * y + a4 * x * y
    return dx, dy

# vypocet stredu
stred_x = a3 / a4 # pocet koristi, za ktere je dravcu porad stejne (dy = 0)
stred_y = a1 / a2 # pocet dravcu, z ktere je korist konstanti (dx = 0)

# =====================================================

def vnitrodruh(u,v):
    du = a1 * u - a2 * u * v - b1 * (u**2)
    dv = - a3 * v + a4 * u * v - b2 * (v**2)
    return du, dv

# stred
D = b1 * b2 + a2 * a4
sx = (a1 * b2 + a2 * a3) / D 
sy = (-b1 * a3 + a1 * a4) / D

# =====================================================

# vykresleni obou grafu v jednom
osa_x = np.linspace(0, 8, 100)
osa_y = np.linspace(0, 8, 100)
X, Y = np.meshgrid(osa_x, osa_y)

# vektorova pole
DX_M, DY_M = mezidruh(X, Y)
speed_mezi = np.sqrt(DX_M**2 + DY_M**2)

DX_V, DY_V = vnitrodruh(X, Y)
speed_vnit = np.sqrt(DX_V**2 + DY_V**2)

# samotne vykreslovani
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Levo - mezidruh
ax1.streamplot(X, Y, DX_M, DY_M, color=speed_mezi, cmap='autumn', linewidth=1.2, density=1.3)

ax1.axhline(stred_y, color='black', linestyle='--', linewidth=2, label='Izoklina kořisti ($dx/dt=0$)')
ax1.axvline(stred_x, color='dimgray', linestyle='-.', linewidth=2, label='Izoklina dravců ($dy/dt=0$)')

ax1.scatter([stred_x], [stred_y], color='black', s=120, zorder=5, 
           label=f'Kritický bod (Střed) [{stred_x:.1f}, {stred_y:.1f}]')
ax1.set_title('Bez vnitrodruhové konkurence', fontsize=12)
ax1.set_xlabel('Populace kořisti ($x$)', fontsize=11)
ax1.set_ylabel('Populace dravců ($y$)', fontsize=11)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right')

# Pravo - i vnitroddruhova konkurence
ax2.streamplot(X, Y, DX_V, DY_V, color=speed_vnit, cmap='winter', linewidth=1.2, density=1.3)

# izokliny (du = 0, dv = 0)
izo_u = (a1 - b1 * osa_x) / a2 # vliv dravců na stagnaci kořisti při vnitrodruhové konkurenci
izo_v = (-a3 + a4 * osa_x) / b2 # minimální kořist nutná pro růst populace dravců při jejich vlastní konkurenci

ax2.plot(osa_x, izo_u, color='black', linestyle='--', linewidth=2, label='Izoklina kořisti ($du/dt=0$)')
ax2.plot(osa_x, izo_v, color='dimgray', linestyle='-.', linewidth=2, label='Izoklina dravců ($dv/dt=0$)')


ax2.scatter([sx], [sy], color='black', s=120, zorder=5, 
           label=f'Kritický bod [{sx:.1f}, {sy:.1f}]')
ax2.set_title('S vnitrodruhovou konkurencí (Stabilizace ekosystému)', fontsize=12)
ax2.set_xlabel('Populace kořisti ($u$)', fontsize=11)
ax2.set_ylabel('Populace dravců ($v$)', fontsize=11)

ax2.set_xlim(0, 8)
ax2.set_ylim(0, 8)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right')

plt.suptitle('Fázové portréty dynamického systému Kořist - Dravec (Lotka-Volterra) bez i s vnitrodruhovou konkurencí', fontsize=14, weight='bold', y=0.96)
plt.tight_layout()
plt.show()
