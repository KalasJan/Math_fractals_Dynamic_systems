#kochova cara

# totez, co je u Kochovy vlocky
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
    p2 = p1 + delta * num.exp(1j *num.pi / 3)  # Otáčení o 60 stupňů pomocí komplexních čísel
    # uhel +pi/3 je smer nahoru, uhel -pi/3 je bezna vlocka
    
    # Rekurzivní volání pro každou část
    # [:-1] + \ vylouci prostredni cast, a spoji dalsi
    return (
        cara(start, p1, hloubka - 1)[:-1]+  
           cara(p1, p2, hloubka - 1)[:-1] + 
           cara(p2, p3, hloubka - 1)[:-1] +
           cara(p3, konec, hloubka - 1)
           )

# navic neni u vlocky
# fce pro kresleni
def vykresli_caru(hloubka):
    start = 0+0j #jsme v komplexnich cislech
    konec = 1+0j
    
    # vytvoreni cary
    linka = cara(start, konec, hloubka)
    
    # kresleni
    mal.figure(figsize=(10, 4))
    mal.plot([p.real for p in linka], [p.imag for p in linka], color="blue")
    mal.axis('equal')
    mal.axis('off')
    mal.title(f"Kochova čára (hloubka {hloubka})")
    mal.show()

# samotne vykresleni
vykresli_caru(1)
