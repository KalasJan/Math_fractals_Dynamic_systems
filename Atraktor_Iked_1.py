# Jak vypada Ikeduv aktraktor
# formou 2 iteraci x_n, y_n

from numpy import sin, cos
import matplotlib.pyplot as mal

# parametry
u = 0.7 # koeficient minimalne 0.6 
iterace = 50000 #pocet iteraci

# pocatecni podminky
x,y = 0, 0

# vykresleni cary
x2, y2 = [x], [y]

# Generování atraktoru
for i in range(iterace):
    t = 0.4 - 6/(1+x**2+y**2)
    nove_x = 1 + u * (x * cos(t) - y * sin(t))
    nove_y = u * (x * sin(t) + y * cos(t))  
    x, y = nove_x, nove_y
    x2.append(x)
    y2.append(y)

# Vykreslení atraktoru
mal.figure(figsize=(10, 6))
mal.plot(x2, y2, 'd', alpha=0.5, markeredgewidth=0.2)
 # markeredgewidth - obrys bodu je tenka cara, alpha - pruhlednost
mal.title(f"Ikedův atraktor, u = {u}")
mal.xlabel("x")
mal.ylabel("y")
mal.show()
