# Kochova vlocka

import matplotlib.pyplot as mal
import numpy as num

# Funkce pro generování jednoho kroku Kochovy křivky
def cara(start, konec, hloubka):
    if hloubka == 0:
        return [start, konec]
    
    # Výpočet dělení úsečky na čtyři body
    delta = (konec - start) / 3
    p1 = start + delta
    p3 = start + 2 * delta
    # Vytvoření bodu p2 jako vrcholu nového trojúhelníku
    p2 = p1 + delta * num.exp(1j * (-1)*num.pi / 3)  # Otáčení o 60 stupňů pomocí komplexních čísel
    # uhel +pi/3 je vnorena vlocka (dovnitr), uhel -pi/3 je bezna vlocka
    
    # Rekurzivní volání pro každou část
    # [:-1] + \ vylouci prostredni cast, a spoji dalsi
    return (
        cara(start, p1, hloubka - 1)[:-1]+  
           cara(p1, p2, hloubka - 1)[:-1] + 
           cara(p2, p3, hloubka - 1)[:-1] +
           cara(p3, konec, hloubka - 1)
           )

# Funkce pro vykreslení celé Kochovy vločky
def vlocka(hloubka):
    # Výchozí body rovnostranného trojúhelníku
    p1 = num.exp(1j * 0)
    p2 = num.exp(1j * 2 * num.pi / 3)
    p3 = num.exp(1j * 4 * num.pi / 3)

    # Vygenerování tří stran vločky
    strana1 = cara(p1, p2, hloubka)
    strana2 = cara(p2, p3, hloubka)
    strana3 = cara(p3, p1, hloubka)

    # Spojení stran do jedné linie
    snow = strana1[:-1] + strana2[:-1] + strana3

    # Vykreslení vločky
    mal.figure(figsize=(8, 8))
    mal.plot([p.real for p in snow], [p.imag for p in snow], color="blue")
    mal.axis('equal')
    mal.axis('off')
    mal.title(f"Kochova vločka (hloubka {hloubka})")
    mal.show()

# Vykreslení Kochovy vločky s hloubkou 4
vlocka(5)
