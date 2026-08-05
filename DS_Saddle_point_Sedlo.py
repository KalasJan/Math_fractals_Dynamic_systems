# Vykresli fazove portrety typu Sedlo

import numpy as np
import matplotlib.pyplot as plt

# Typ 1 - matice J = [[L1,0],[0,L2]], L1 * L2 < 0

def soustava(x,y):
    dx = -1*x
    dy = 2*y
    return dx,dy #L1 = -1, L2 = 2

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
plt.scatter(0, 0, color='black', s=150, zorder=5)

# Cisteni grafu
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')
plt.title('Fázový portrét lineárního systému: Sedlo pro 2 ruzna vlastni $\lambda_1 = -1$ a $\lambda_2 = 2$ ', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# Typ 2 - matice J = [[L1,0],[0,L1]], L1  < 0

J2 = np.array([[1,2],[3,-1]])

# Vytvoření mříže bodů ve fázovém prostoru
x2 = np.linspace(-1, 1, 100)
y2 = np.linspace(-1, 1, 100)
X2, Y2 = np.meshgrid(x2, y2)

# matice radek1 = X, radek2 = Y
predmatice = np.vstack([X2.ravel(), Y2.ravel()])

# soucin matic
soucin = J2 @ predmatice

# navrat do mrize
dX2 = soucin[0].reshape(X2.shape)
dY2 = soucin[1].reshape(Y2.shape)

# Samotné vykreslení
plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX2**2 + dY2**2)

# streamplot vykreslí trajektorie i se šipkami
plt.streamplot(X2, Y2, dX2, dY2, color=rychlost, cmap='coolwarm', density=1.2)
plt.scatter(0, 0, color='black', s=120, zorder=5) # kriticky bod

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(r'Fázový portrét (Sedlo) generovaný maticově $J \cdot \vec{x}$')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()