#vykresli Henonuv atraktor

import matplotlib.pyplot as mal

# Parametry (nejcasteji a = 1.4, b = 0.3)
a = 1.39 # 1 - 1.4
b = 0.21 # 0.2 - 0.3

# Počáteční podmínky
x, y = 0, 0

# Počet iterací
iterace = 10000

# vykresleni cary
x2, y2 = [], []

# Generování atraktoru
for _ in range(iterace):
    nove_x = 1 - a * x**2 + y
    nove_y = b * x
    x, y = nove_x, nove_y
    x2.append(x)
    y2.append(y)

# Vykreslení atraktoru
mal.figure(figsize=(8, 8))
mal.plot(x2, y2, 'o', markersize=0.5, color='blue')
mal.title("Henonův atraktor")
mal.xlabel("x")
mal.ylabel("y")
mal.show()