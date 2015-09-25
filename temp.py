# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sinteg

plt.figure(1)
plt.clf()

datos=np.genfromtxt('sun_AM0.dat',float)

longitud=datos[:,0]*10 #Angstroms
flujo=datos[:,1]*10**11

plt.plot(np.log10(longitud), np.log10(flujo))   

plt.xlabel('x log10[Longitud de Onda (Angstrom)]')
plt.ylabel('y log10[Flujo (CGS)]')
plt.title('Espectro del Sol (Flujo vs Longitud de Onda)')
plt.legend()

"""
Dado que x1-x0 = 20 = constante podemos considerarlo como un trazador lineal
por lo que podemos aplicar el metodo del trapecio
"""
def integraltrap(x,y):
    """
    Recibe preimagen e imagen de funcion con y 
    encuentra integral utilizando el metodo del trapezio
    """
    contador=0
    integral=0
    trapecio=0
    while contador<len(x)-1:
        trapecio=(y[contador]+y[contador+1])*(x[contador+1]-x[contador])/2 
        integral=integral+trapecio
        contador=contador+1
    return integral

sol= integraltrap(longitud,flujo)

#superficie esférica a la distancia en que se encuentra la Tierra 2.81e23 m2
ctesolar=sol*10**-12 # en W/m2

luminosidadtot= ctesolar*2.81e23

integralcalc=sinteg.trapz(flujo,longitud)
