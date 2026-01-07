# Mandelbrotova mnozina
# z_(n+1)=z_n^2+C, kde cisla jsou komplexni a abs(z) <=2

import numpy as num #numerika
import matplotlib.pyplot as vyk

vyska, sirka = 800, 800 #rozliseni
min_x, max_x = -1.5, 1 #jsme v rovine abs(z)<=2
min_y, max_y = -1.5, 1 # nechceme celou rovinu, staci kousek
iter_max = 100 # max pocet iteraci

# mrizka v C
x = num.linspace(min_x, max_x, vyska)
y = num.linspace(min_y, max_y, sirka)
X, Y = num.meshgrid(x,y) # mrizka vsech kombinaci x,y
C = X + Y*1j # tvar komplexniho cisla, musi byt 1j

# iterace
Z = num.zeros_like(C, dtype=complex) # jsme v komplexnich cislech
iterace = num.zeros(C.shape, dtype=int)
#vsechny hodnoty o stejne velikosti, zaciname 0
#Cshape - vraceni po iteraci, , dtype - cela cisla

# vypocet mnoziny
for k in range (iter_max):
    obraz = num.abs(Z)<=2 # abs hodnota max 2
    Z[obraz] = Z[obraz]**2+C[obraz] #vzorec mnoziny
    iterace[obraz] = k

# vykresleni mnoziny
vyk.imshow(iterace, extent=(min_x, max_x, min_y, max_y), cmap='plasma')
# imshow (iterace), extent(rozsah), cmap(1 iterace = 1 barva)
vyk.colorbar(label='Počet iterací')
vyk.title("Mandelbrotova množina")
vyk.xlabel("Reálná část")
vyk.ylabel("Imaginární část")
vyk.show()

