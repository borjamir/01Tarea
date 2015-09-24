# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sinteg

plt.figure(1)
plt.clf()

datos=np.genfromtxt('sun_AM0.dat',float)

longitud=datos[:,0]*10 #Angstroms
flujo=datos[:,1]*10**10

plt.plot(np.log10(longitud), np.log10(flujo))   

plt.xlabel('x log10[Longitud de Onda (Angstrom)]')
plt.ylabel('y log10[Flujo (CGS)]')
plt.title('Espectro del Sol (Flujo vs Longitud de Onda)')
plt.legend()

"""
Dado que x1-x0 = 2 = constante podemos considerarlo como un trazador lineal
por lo que podemos aplicar el metodo del trapecio
"""

contador=0
integral=0
trapecio=0
while contador<1696:
    trapecio=flujo[contador]+flujo[contador+1] #no multiplico porque delta x=2
    integral=integral+trapecio
    contador=contador+1
print integral

integralcalc=sinteg.trapz(flujo,longitud)
