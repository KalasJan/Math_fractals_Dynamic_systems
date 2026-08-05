# Vykresli fazovy portrety typu Rovina kritickych bodu

# Matice J = ([[0,0],[0,0]])

import numpy as np
import matplotlib.pyplot as plt

def soustava(x,y):
    dx = np.zeros_like(x) # protoze ma byt 0 a vysledek je prazdny graf
    dy = np.zeros_like(y) # protoze ma byt 0 a vysledek je prazdny graf
    return dx, dy 

# Vytvoření mříže bodů ve fázovém prostoru
x = np.linspace(-0.5, 0.5, 100)
y = np.linspace(-0.5, 0.5, 100)
X, Y = np.meshgrid(x, y)

# Výpočet rychlostí (vektorů) v každém bodě
dX, dY = soustava(X, Y)

plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX**2 + dY**2)
plt.streamplot(X, Y, dX, dY, color=rychlost, cmap='coolwarm', density=1.4, linewidth=1.5)
# streamplot - trajektorie se sipkami smeru

# Vykreslení stabilního pole šipek
plt.quiver(X, Y, dX, dY, color='crimson', scale=50)

# Cisteni grafu
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')
plt.title('Fázový portrét lineárního systému typu Rovina kritickych bodu', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# Každý bod v celém prostoru je kritický (rovnovážný). Rychlost je všude nulová.