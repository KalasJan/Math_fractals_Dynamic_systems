#jak vypada Weierstrasseova funkce
# je vsude spojita, nikde diferencovatelna (nema derivaci)
# f(x) = suma a^n*cos(b^n*pi*x), kde n in [0, oo) a dalsi podminky

import numpy as num
import matplotlib.pyplot as mal

# koeficienty
a = num.sin(num.pi/4) # koeficient mezi 0, 1 
b = 3*num.sin(num.pi/3) # cislo vetsi nez 1
N = 100 # pocet clenu (numericky to nejde do + nekonecna)
x = num.linspace(0,1, 1000) # start, cil, pocet bodu

# definice fce
def f(x,a,b,N):
    vysledek = num.zeros_like(x)
    for n in range (N):
        vysledek += a**n* num.cos(b**n * num.pi * x)
    return vysledek

# hodnoty funkce
y = f(x, a, b, N)

# kresleni funkce
mal.plot(x, y,
         label = f'a = {a:.2f} \n b = {b:.2f} \n N = {N}.') # label je k legende
# \n na kazdy radek, :.2f zaokrouhleni na 2 desetiny
mal.title("Weierstrassova funkce")
mal.xlabel("x")
mal.ylabel("f(x)")
mal.grid(True)
mal.legend()
mal.show()