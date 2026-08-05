# Vykresli vsechny 4 fazove portrety typu Ohnisko

# mame matici J = ([[a,-b],[b,a]]) a vlasnti cisla ve tvaru a +-i*b

import numpy as np
import matplotlib.pyplot as plt

# Typ 1 - a > 0, b > 0 (napr a = 3, b = 2)

J1 = np.array([[3, -2], [2, 3]])
u1 = np.array([4, 2]) # kriticky bod nebube [0,0]

# vypocet kritickeho bodu
x_kriticky, y_kriticky = np.linalg.solve(J1, -u1)

# Vytvoření mříže bodů ve fázovém prostoru
x1 = np.linspace(x_kriticky-0.5, x_kriticky+0.5, 100)
y1 = np.linspace(y_kriticky-0.5, y_kriticky+0.5, 100)
X1, Y1 = np.meshgrid(x1, y1)

# matice radek1 = X, radek2 = Y
predmatice = np.vstack([X1.ravel(), Y1.ravel()])

# soucin matic
soucin = J1 @ predmatice + u1.reshape(-1,1)

# navrat do mrize
dX1 = soucin[0].reshape(X1.shape)
dY1 = soucin[1].reshape(Y1.shape)

# Samotné vykreslení
plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX1**2 + dY1**2)

# streamplot vykreslí trajektorie i se šipkami
plt.streamplot(X1, Y1, dX1, dY1, color=rychlost, cmap='coolwarm', density=1.2)
plt.scatter(x_kriticky, y_kriticky, color='black', s=120, zorder=5, label=f'Kritický bod je [{x_kriticky:.2f}, {y_kriticky:.2f}]') # kriticky bod

plt.axhline(y_kriticky, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x_kriticky, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(x1.min(), x1.max())
plt.ylim(y1.min(), y1.max())
plt.title(r'Fázový portrét (Ohnisko-zřídlo) generovaný maticově $J \cdot \vec{x} + \vec{u}$')
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# Typ 2: a > 0, b < 0 (napr a = 3, b = -2)

J2 = np.array([[3, 2], [-2, 3]])
u2 = np.array([1, 2]) # kriticky bod nebube [0,0]

# vypocet kritickeho bodu
x_kriticky2, y_kriticky2 = np.linalg.solve(J2, -u2)

# Vytvoření mříže bodů ve fázovém prostoru
x2 = np.linspace(x_kriticky2-0.5, x_kriticky2+0.5, 100)
y2 = np.linspace(y_kriticky2-0.5, y_kriticky2+0.5, 100)
X2, Y2 = np.meshgrid(x2, y2)

# matice radek1 = X, radek2 = Y
predmatice2 = np.vstack([X2.ravel(), Y2.ravel()])

# soucin matic
soucin2 = J2 @ predmatice2 + u2.reshape(-1,1)

# navrat do mrize
dX2 = soucin2[0].reshape(X2.shape)
dY2 = soucin2[1].reshape(Y2.shape)

# Samotné vykreslení
plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX2**2 + dY2**2)

# streamplot vykreslí trajektorie i se šipkami
plt.streamplot(X2, Y2, dX2, dY2, color=rychlost, cmap='coolwarm', density=1.2)
plt.scatter(x_kriticky2, y_kriticky2, color='black', s=120, zorder=5, label=f'Kritický bod je [{x_kriticky2:.2f}, {y_kriticky2:.2f}]') # kriticky bod

plt.axhline(y_kriticky2, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x_kriticky2, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(x2.min(), x2.max())
plt.ylim(y2.min(), y2.max())
plt.title(r'Fázový portrét (Ohnisko-zřídlo) generovaný maticově $J \cdot \vec{x} + \vec{u}$')
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# Typ 3: a < 0, b > 0 (napr a = -3, b = 2)

J3 = np.array([[-3, -2], [2, -3]])
u3 = np.array([0, 2]) # kriticky bod nebube [0,0]

# vypocet kritickeho bodu
x_kriticky3, y_kriticky3 = np.linalg.solve(J3, -u3)

# Vytvoření mříže bodů ve fázovém prostoru
x3 = np.linspace(x_kriticky3-0.5, x_kriticky3+0.5, 100)
y3 = np.linspace(y_kriticky3-0.5, y_kriticky3+0.5, 100)
X3, Y3 = np.meshgrid(x3, y3)

# matice radek1 = X, radek2 = Y
predmatice3 = np.vstack([X3.ravel(), Y3.ravel()])

# soucin matic
soucin3 = J3 @ predmatice3 + u3.reshape(-1,1)

# navrat do mrize
dX3 = soucin3[0].reshape(X3.shape)
dY3 = soucin3[1].reshape(Y3.shape)

# Samotné vykreslení
plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX3**2 + dY3**2)

# streamplot vykreslí trajektorie i se šipkami
plt.streamplot(X3, Y3, dX3, dY3, color=rychlost, cmap='coolwarm', density=1.2)
plt.scatter(x_kriticky3, y_kriticky3, color='black', s=120, zorder=5, label=f'Kritický bod je [{x_kriticky3:.2f}, {y_kriticky3:.2f}]') # kriticky bod

plt.axhline(y_kriticky3, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x_kriticky3, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(x3.min(), x3.max())
plt.ylim(y3.min(), y3.max())
plt.title(r'Fázový portrét (Ohnisko-výlevka) generovaný maticově $J \cdot \vec{x} + \vec{u}$')
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# Typ 4: a < 0, b < 0 (napr a = -3, b = -1)

J4 = np.array([[-3, 1], [-1, -3]])
u4 = np.array([-1, 2]) # kriticky bod nebube [0,0]

# vypocet kritickeho bodu
x_kriticky4, y_kriticky4 = np.linalg.solve(J4, -u4)

# Vytvoření mříže bodů ve fázovém prostoru
x4 = np.linspace(x_kriticky4-0.5, x_kriticky4+0.5, 100)
y4 = np.linspace(y_kriticky4-0.5, y_kriticky4+0.5, 100)
X4, Y4 = np.meshgrid(x4, y4)

# matice radek1 = X, radek2 = Y
predmatice4 = np.vstack([X4.ravel(), Y4.ravel()])

# soucin matic
soucin4 = J4 @ predmatice4 + u4.reshape(-1,1)

# navrat do mrize
dX4 = soucin4[0].reshape(X4.shape)
dY4 = soucin4[1].reshape(Y4.shape)

# Samotné vykreslení
plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dX4**2 + dY4**2)

# streamplot vykreslí trajektorie i se šipkami
plt.streamplot(X4, Y4, dX4, dY4, color=rychlost, cmap='coolwarm', density=1.2)
plt.scatter(x_kriticky4, y_kriticky4, color='black', s=120, zorder=5, label=f'Kritický bod je [{x_kriticky4:.2f}, {y_kriticky4:.2f}]') # kriticky bod

plt.axhline(y_kriticky4, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x_kriticky4, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(x4.min(), x4.max())
plt.ylim(y4.min(), y4.max())
plt.title(r'Fázový portrét (Ohnisko-výlevka) generovaný maticově $J \cdot \vec{x} + \vec{u}$')
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

