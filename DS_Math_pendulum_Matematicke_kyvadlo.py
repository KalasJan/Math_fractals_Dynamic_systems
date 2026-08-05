# Nelinearni Dynamicky system - Matematicke kyvadlo

import numpy as np
import matplotlib.pyplot as plt

# definice rovnice
def kyvadlo(x,y):
    dx = y
    dy = -np.sin(x)
    return dx, dy

# Vytvoření mříže bodů (rozsah od cca -1.5*pi do 1.5*pi, aby graf seděl s obrázkem)
x = np.linspace(-10, 10, 1000)
y = np.linspace(-2.5, 2.5, 1000)
X, Y = np.meshgrid(x, y)

dX, dY = kyvadlo(X, Y)

plt.figure(figsize=(11, 6))

# Vykreslení proudnic (trajektorií) černou barvou se šipkami
plt.streamplot(X, Y, dX, dY, color='black', density=1.2, linewidth=1.0, zorder=1)

# ZVÝRAZNĚNÍ SEPARATRISY (oddeuje "vnitrni" a "vnejsi" cast)
x_sep = np.linspace(-10, 10, 1000)
vnitrek = 2 * (1 + np.cos(x_sep))
y_sep_top = np.sqrt(np.maximum(0, vnitrek))
y_sep_bottom = -np.sqrt(np.maximum(0, vnitrek))

plt.plot(x_sep, y_sep_top, color='black', linewidth=3.0, zorder=2)
plt.plot(x_sep, y_sep_bottom, color='black', linewidth=3.0, zorder=2)

# Stred, sedlo
stredy_x = [-2 * np.pi, 0, 2 * np.pi]
stredy_y = [0, 0, 0]

sedla_x = [-3*np.pi, -np.pi, np.pi, 3*np.pi]
sedla_y = [0, 0, 0, 0]

# Vykreslení výrazných bodů 
plt.scatter(stredy_x, stredy_y, color='blue', s=150, zorder=3, label='Střed (Stabilní poloha)')
plt.scatter(sedla_x, sedla_y, color='black', s=150, facecolors='red', edgecolors='black', linewidth=2.5, zorder=3, label='Sedlo (Nestabilní poloha)')
# facecolor = vypln kola

# 6. Začištění a popisky os v LaTeXu
plt.xlim(-10, 10)
plt.ylim(-2.5, 2.5)

# Nastavení hezkých popisků na ose X v násobcích pí
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])

plt.xlabel(r'$\alpha$ (Úhel kyvadla)', fontsize=14)
plt.ylabel(r'$\dot{\alpha}$ (Úhlová rychlost)', fontsize=14)
plt.title('Fázový portrét nelineárního matematického kyvadla', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.4)

plt.show()