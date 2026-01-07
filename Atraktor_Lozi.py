#Loziho atraktor

import numpy as num
import matplotlib.pyplot as mal

# Parametry
a = 1.7
b = 0.5
c = 0.7

# Počáteční podmínky
x0 = 0
y0 = 0

# Počet iterací
iterace = 10000

# Inicializace polí pro x a y
nove_x = num.zeros(iterace)
nove_y = num.zeros(iterace)

# Nastavení počátečních hodnot
nove_x[0] = x0
nove_y[0] = y0

# Iterace pro hodnoty atraktoru
for k in range(1, iterace):
    nove_x[k] = 1 - a * nove_x[k-1]**2 + b * nove_y[k-1]
    nove_y[k] = c * nove_x[k-1]
    
    # omezeni (proti Overflow)
    maxi = 2
    nove_x[k] = num.clip(nove_x[k], -maxi, maxi)
    nove_y[k] = num.clip(nove_y[k], -maxi, maxi)


# Vykreslení atraktoru
mal.figure(figsize=(8, 6))
mal.plot(nove_x, nove_y, color='blue', linewidth=1, label = f'a = {a}\nb = {b}\nc = {c}y\n[{x0},{y0}]')
mal.title("Loziho Atraktor")
mal.xlabel("x")
mal.ylabel("y")
mal.legend()
mal.show()
