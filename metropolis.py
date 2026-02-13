import numpy as np
import random as random

def metropolis(spins, adx, k, T, J):
    #posicion do spin seleccionado
    posicion = np.random.randint(0, len(spins))
        
    s = spins[posicion] #valor do spin seleccionado
    vec = adx[posicion] #Posición dos veciños

    #Enerxía debido ó spin seleccionado
    E=0
    for j in vec:
        E = E - J*np.cos(s-spins[j])

    #Escollemos un novo valor de spin asegurándonos de que non se repita o valor sn=s
    sn = s
    while sn==s:
        sn = random.choice(k) #valor novo do spin

    En = 0
    for j in vec:
        En = En - J*np.cos(sn-spins[j])

    deltaE = En-E #variación da enerxía

    if deltaE<0:
        spins[posicion] = sn
    elif np.exp(-deltaE/T)>random.random():
        spins[posicion] = sn
    return spins








