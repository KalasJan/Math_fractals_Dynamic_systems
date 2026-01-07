# Ikeda verze 2
# pomoci 1 iterace z_n

import numpy as num
import matplotlib.pyplot as mal

# promenne:
a = 0.4
b = 0.9
c = 0.7

# pocet iteraci
iterace = 10000

# pocatecni hodnota Z_0
Z = num.complex(0, 0) 

# uchovani hodnot
hodnoty_Z = []

# iterace
for p in range (iterace):
    Z = a + b * Z * num.exp(1j * (num.abs(Z)**2 + c))
    hodnoty_Z.append(Z)
    
# rozklad na Re(Z) a Im(Z)
hodnoty_Z = num.array(hodnoty_Z)
real = hodnoty_Z.real
imag = hodnoty_Z.imag

# vykresleni
mal.figure(figsize=(6,6))
mal.plot(real, imag, marker='o', markersize=3, linestyle='-', color='b')
mal.title(f"Ikedův atraktor, a={a}, b={b}, c={c}")
mal.xlabel("Reálná složka")
mal.ylabel("Imaginární složka")
mal.grid(True)
mal.show()