# nakresli Cantorovu mnozinu, diskontinuum

import matplotlib.pyplot as mal

def mnozina(x, y, delka, sirka):
    # Podmínka pro zastavení rekurze (pokud jsme dosáhli požadované hloubky)
    if sirka == 0:
        return

    # Nakreslení čáry pro aktuální úroveň
    mal.plot([x, x + delka], [y, y], 'k', lw=10)  # 'k' je černá barva, 'lw' je šířka čáry
    
    # Vypočítání nových parametrů pro další úroveň
    dalsi_rada = y - 1  # Posunutí dolů pro každou další úroveň
    dalsi_uroven = delka / 3  # Rozdělení délky na třetiny

    # Rekurzivní volání pro levý a pravý segment
    mnozina(x, dalsi_rada, dalsi_uroven, sirka - 1)           # Levý segment
    mnozina(x + 2 * dalsi_uroven, dalsi_rada, dalsi_uroven, sirka - 1)  # Pravý segment

# Nastavení parametrů grafu
mal.figure(figsize=(10, 6))
mal.title("Cantorova množina")

# Spuštění rekurzivního vykreslování Cantorovy množiny
mnozina(0, 0, 10, 5)  # Počáteční pozice x, y, délka, a počet úrovní

# Úprava zobrazení grafu
# plt.gca().invert_yaxis()  # Obrácení osy y (vyšší úrovně nahoře)
mal.axis('off')           # Skrytí os
mal.show()

 
