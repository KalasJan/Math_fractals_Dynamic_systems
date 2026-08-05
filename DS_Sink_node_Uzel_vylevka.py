# Vykresli 3 fazove portrety typu Uzel-Vylevka

import numpy as np
import matplotlib.pyplot as plt

# Typ 1 - matice J = [[L1,0],[0,L2]], L1, L2  < 0

def soustava(x,y):
    dx = -1*x
    dy = -2*y
    return dx,dy #L1 = -1, L2 = -2

# Vytvoření mříže bodů ve fázovém prostoru
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
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
plt.title('Fázový portrét lineárního systému: Uzel-výlevka pro 2 ruzna vlastni $\lambda < 0$ ', fontsize=12)
# plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# Typ 2 - matice J = [[L1,0],[0,L1]], L1  < 0

J = np.array([[-0.5,0],[0,-0.5]])

# Vytvoření mříže bodů ve fázovém prostoru
x2 = np.linspace(-2, 2, 100)
y2 = np.linspace(-2, 2, 100)
X2, Y2 = np.meshgrid(x2, y2)

# matice radek1 = X, radek2 = Y
predmatice = np.vstack([X2.ravel(), Y2.ravel()])

# soucin matic
soucin = J @ predmatice

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
plt.title(r'Fázový portrét (Uzel-výlevka) generovaný čistě maticově $J \cdot \vec{x}$ pro $\lambda = -0.5$')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# Typ 3 - matice J = [[L1,1],[0,L1]], L1 < 0

def soustava3(x,y):
    dx3 = -0.5*x+ 1*y
    dy3 = -0.5*y
    return dx3,dy3 

# Vytvoření mříže bodů ve fázovém prostoru
x3 = np.linspace(-0.5, 0.5, 100)
y3 = np.linspace(-0.5, 0.5, 100)
X3, Y3 = np.meshgrid(x3, y3)

# Výpočet rychlostí (vektorů) v každém bodě
dX3, dY3 = soustava3(X3, Y3)

plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX3**2 + dY3**2)
plt.streamplot(X3, Y3, dX3, dY3, color=rychlost, cmap='coolwarm', density=1.2, linewidth=1.5)
# streamplot - trajektorie se sipkami smeru

# kriticky bod
plt.scatter(0, 0, color='black', s=150, zorder=5)

# Cisteni grafu
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')
plt.title('Fázový portrét lineárního systému: Uzel-výlevka pro $\lambda = -0.5$ ', fontsize=12)
# plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()