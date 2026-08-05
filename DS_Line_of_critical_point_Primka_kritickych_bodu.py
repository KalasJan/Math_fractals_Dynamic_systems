# Vykresli fazovy portrety typu Primka ne/stabilnich kritickych bodu
# Matice J = ([[0,0],[0,a]]) a> 0 nestabilni, a < 0 stabilni
# pozn p - kladne cislo, n - zaporne cislo

import numpy as np
import matplotlib.pyplot as plt

# nestabilni

def soustavap(xp,yp):
    dxp = np.zeros_like(Xp) # protoze ma byt 0 a vysledek je prazdny graf
    dyp = 2*yp
    return dxp, dyp # a>0

# Vytvoření mříže bodů ve fázovém prostoru
xp = np.linspace(-2, 2, 100)
yp = np.linspace(-0.5, 0.5, 100)
Xp, Yp = np.meshgrid(xp, yp)

# Výpočet rychlostí (vektorů) v každém bodě
dXp, dYp = soustavap(Xp, Yp)

plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dXp**2 + dYp**2)
plt.streamplot(Xp, Yp, dXp, dYp, color=rychlost, cmap='coolwarm', density=0.4, linewidth=1.5)
# streamplot - trajektorie se sipkami smeru

# Vykreslení stabilního pole šipek
plt.quiver(Xp, Yp, dXp, dYp, color='crimson', scale=50)

# Cisteni grafu
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')
plt.title('Fázový portrét lineárního systému typu Přímka nestabilnich bodů pro  $ a = 2$ ', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# -----------------------------------------------------------------

# stabilni 

def soustavan(xn,yn):
    dxn = np.zeros_like(Xn) # protoze ma byt 0 a vysledek je prazdny graf
    dyn = -5*yn
    return dxn, dyn # a>0

# Vytvoření mříže bodů ve fázovém prostoru
xn = np.linspace(-2, 2, 100)
yn = np.linspace(-0.5, 0.5, 100)
Xn, Yn = np.meshgrid(xn, yn)

# Výpočet rychlostí (vektorů) v každém bodě
dXn, dYn = soustavan(Xn, Yn)

plt.figure(figsize=(8, 8))
rychlost = np.sqrt(dXn**2 + dYn**2)
plt.streamplot(Xn, Yn, dXn, dYn, color=rychlost, cmap='coolwarm', density=0.4, linewidth=1.5)
# streamplot - trajektorie se sipkami smeru

# Vykreslení stabilního pole šipek
plt.quiver(Xn, Yn, dXn, dYn, color='crimson', scale=50)

# Cisteni grafu
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')
plt.title('Fázový portrét lineárního systému typu Přímka stabilnich bodů pro  $ a = -5 $ ', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()