# Vykresli fazovy portrety typu Stred/Centre
# Matice J = ([[0,-b],[b,0]])

import numpy as np
import matplotlib.pyplot as plt

def soustava(x,y):
    dx = -2*y
    dy = 2*x
    return dx, dy # b= 2

# Vytvoření mříže bodů ve fázovém prostoru
x = np.linspace(-0.1, 0.1, 100)
y = np.linspace(-0.1, 0.1, 100)
X, Y = np.meshgrid(x, y)

# Výpočet rychlostí (vektorů) v každém bodě
dX, dY = soustava(X, Y)

plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX**2 + dY**2)
plt.streamplot(X, Y, dX, dY, color=rychlost, cmap='coolwarm', density=1.2, linewidth=1.5)
# streamplot - trajektorie se sipkami smeru

# kriticky bod
plt.scatter(0, 0, color='black', s=150, zorder=5, label = 'b=2')

# Cisteni grafu
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')
plt.title('Fázový portrét lineárního systému typu Střed pro  $ b = 2$ ', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# pozn: b < 0 jen otoci smer rotace
