# Vykresli fazovy portret zadany systemem ODR

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

x, y = sm.symbols('x y', real=True)

# definice soustavy
dx = - x**3 + x * y
dy = -y +y**2 + x*y -x**3

# stacionarni body (dx = 0, dy = 0)

kriticke = sm.solve([dx, dy], (x, y), dict=True)

# soustava pomoci Jacobiho matice
matice = sm.Matrix([dx, dy])
jacob = matice.jacobian([x, y])

points = []

for idx, bod in enumerate(kriticke):
    bx = float(bod.get(x, 0.0))
    by = float(bod.get(y, 0.0))
    
    # body do Jakobianu a vypocet vlastnich cisel
    Jac_bod = jacob.subs({x: bx, y: by})
    vlastni = list(Jac_bod.eigenvals().keys())
    
    # prevod na komplexni cisla
    lam1_real = float(sm.re(vlastni[0]).evalf())
    lam1_imag = float(sm.im(vlastni[0]).evalf())
    
    lam2_real = float(sm.re(vlastni[1]).evalf()) if len(vlastni) > 1 else lam1_real
    lam2_imag = float(sm.im(vlastni[1]).evalf()) if len(vlastni) > 1 else lam1_imag
 
    
    # klasifikace stability podle real a imag
    infty = len(bod) < 2 or any(hasattr(val, 'free_symbols') and val.free_symbols for val in bod.values())
    
    if lam1_real == 0 and lam2_real == 0 and lam1_imag == 0:
        if infty:
            # Pokud je hodnost Jacobianu 1, body tvoří přímku. Pokud 0, tvoří celou rovinu.
            hodnost = Jac_bod.rank()
            if hodnost == 1:
                typ = "Přímka kritických bodů (Nekonečně mnoho řešení)"
                barva = "purple"
            elif hodnost == 0:
                typ = "Rovina kritických bodů (Celý prostor stojí)"
                barva = "indigo"
        else:
            typ = "Izolovaný degenerovaný bod (Sedlo-uzel)"
            barva = "darkviolet"
    elif (lam1_real == 0 or lam2_real == 0) and infty:
        typ = "Přímka kritických bodů (Nekonečně mnoho řešení)"
        barva = "purple"
    elif lam1_imag != 0:
        if lam1_real < 0:
            typ = "Stabilní ohnisko (Spirála dovnitř)"
            barva = "black"
        elif lam1_real > 0:
            typ = "Nestabilní ohnisko (Spirála ven)"
            barva = "orange"
        else:
            typ = "Střed (Uzavřené cykly)"
            barva = "blue"
    else:
        if lam1_real * lam2_real < 0:
            typ = "Nestabilní sedlo"
            barva = "crimson"
        elif lam1_real < 0 and lam2_real < 0:
            typ = "Stabilní uzel (Výlevka)"
            barva = "darkgreen"
        else:
            typ = "Nestabilní uzel (Zřídlo)"
            barva = "magenta"
        
    print(f"Bod P{idx+1} = [{bx:.2f}, {by:.2f}] -> Vlastní čísla: {lam1_real:.2f} + {lam1_imag:.2f}i, {lam2_real:.2f} + {lam2_imag:.2f}i -> Typ: {typ}")
    points.append((bx, by, barva, f"P{idx+1}: {typ} [{bx:.1f}, {by:.1f}]"))
    
# numerika pro graf # mrizka na [-3,3]x [-3,3] nebo kolem bodu
if points:
    all_x = [b[0] for b in points]
    all_y = [b[1] for b in points]
    x_min, x_max = min(all_x) - 1.5, max(all_x) + 1.5
    y_min, y_max = min(all_y) - 1.5, max(all_y) + 1.5
else:
    x_min, x_max, y_min, y_max = -3, 3, -3, 3    
    
# Vytvoření mříže bodů ve fázovém prostoru
gr_x = np.linspace(x_min, x_max, 100)
gr_y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(gr_x, gr_y)

fdx = sm.lambdify((x, y), dx, 'numpy')
fdy = sm.lambdify((x, y), dy, 'numpy')

DX = fdx(X,Y)
DY = fdy(X,Y)

rychlost = np.sqrt(DX**2 + DY**2)

# Kresleni

plt.figure(figsize=(9, 9))

# proudnice (smer toku)
plt.streamplot(X, Y, DX, DY, color=rychlost, cmap='coolwarm', density=1.3, linewidth=1.5)
    
# osy
# Základní osy x=0, y=0 na pozadí
plt.axhline(0, color='gray', linewidth=1.0, linestyle='-', alpha=0.3)
plt.axvline(0, color='gray', linewidth=1.0, linestyle='-', alpha=0.3)

# primky kritickych bodu, pokud nastanou
if any("Přímka" in p[3] for p in points):
    barva_primky = [p[2] for p in points if "Přímka" in p[3]][0]
    plt.contour(X, Y, rychlost, levels=[0.05], colors=barva_primky, linewidths=4, alpha=0.8, zorder=4)
    plt.plot([], [], color=barva_primky, linewidth=4, label="Přímka klidu (Vše stojí)")

for bx, by, barva, popisek in points:
    plt.scatter([bx], [by], color=barva, s=150, zorder=5, label=popisek)
    plt.axhline(by, color=barva, linewidth=0.8, linestyle='--', alpha=0.3)
    plt.axvline(bx, color=barva, linewidth=0.8, linestyle='--', alpha=0.3)

plt.xlabel('Stavová proměnná $x$')
plt.ylabel('Stavová proměnná $y$')

plt.title(f'Fázový portrét daný systémem ODR \n $dx/dt = {sm.latex(dx)}$  |  $dy/dt = {sm.latex(dy)}$', fontsize=11, pad=15, weight='bold')
plt.grid(True, linestyle=':', alpha=0.5)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc = 'upper right', frameon=True, shadow=True, fontsize=9)

plt.show()