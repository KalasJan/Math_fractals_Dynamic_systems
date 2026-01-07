# nakreslete Sierpinskeho trojuhelnik

import matplotlib.pyplot as mal
import numpy as np

def sier(x, y, velikost, hloubka):
    # Podmínka pro zastavení rekurze
    # hloubka - pocet rekurzi
    if hloubka == 0:
        # Vykreslení trojúhelníku, když dosáhneme požadované hloubky
        uhel = np.array([[x, y], 
                             [x + velikost, y], 
                             [x + velikost / 2, y + np.sqrt(3) * velikost / 2], 
                             [x, y]])  # Vytvoření trojúhelníku
        mal.fill(uhel[:, 0], uhel[:, 1], color="green", edgecolor="black")  # Vykreslení trojúhelníku
    else:
        # Rekurzivní volání pro 3 menší trojúhelníky
        sier(x, y, velikost / 2, hloubka - 1)  # Levý dolni trojúhelník
        sier(x + velikost / 2, y, velikost / 2, hloubka - 1)  # Pravý dolni trojúhelník
        sier(x + velikost / 4, y + np.sqrt(3) * velikost / 4, velikost / 2, hloubka - 1)  # Horní trojúhelník

# Nastavení parametrů grafu
mal.figure(figsize=(2, 2))
mal.title("Sierpińskiho trojúhelník")

# Počáteční parametry: počáteční bod (x, y), velikost trojúhelníku a hloubka rekurze
sier(0, 0, 100, 5)

# Úprava zobrazení grafu
mal.axis('equal')  # Zajištění správného poměru os
mal.axis('off')    # Skrytí os
mal.show()
