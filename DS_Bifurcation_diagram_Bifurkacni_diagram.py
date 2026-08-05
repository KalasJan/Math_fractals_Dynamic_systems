# Vykreslete Bifurkacni ddiagram
# x(n+1) = r * x(n) * (1 - x(n))

import numpy as np
import matplotlib.pyplot as plt

iterations = 10000 # celkem iteraci
last = 200 # ktere se budou kreslit

# rozsah parametru r (mezi 2.5 - 4.2)
n_r = 10000
r_val = np.linspace(2.5, 4.2, n_r)

# x(0), r = 1/2
x = 1/2 * np.ones(n_r)

# tvorba grafu
fig = plt.subplots(figsize=(12, 8))

# iterace
for i in range (iterations):
    x = r_val * x * (1 - x) # rovnice
    
    # pro vykresleni
    if i >= (iterations - last):
        plt.scatter(r_val, x, color='black', s=0.05, alpha=0.1)
        
# vizualizace grafu
plt.title('Bifurkační diagram logistické mapy (Přechod do chaosu)', fontsize=14)
plt.xlabel('Parametr růstu (r)', fontsize=12)
plt.ylabel('Ustálený stav populace (x)', fontsize=12)
plt.xlim(2.5, 4.0)
plt.ylim(0, 1)
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()