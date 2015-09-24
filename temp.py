# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

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