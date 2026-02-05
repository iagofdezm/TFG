import numpy as np

def enerxia_total(spins, adx, J):
    #Inicializamos o contador de enerxia
    E=0
    for i in range(len(spins)):
        s = spins[i]
        vec = adx[i] #Posición dos veciños
        for j in vec:
            E = E - J*np.cos(s-spins[j])
    return E/2.0

def E_spin(posicion, spins, adx, J):
    E=0 #Inicialización da variable
    #A posición será o índice no vector 1D
    s=spins[posicion]
    vec = adx[posicion] #Posición dos veciños
    for j in vec:
        E = E - J*np.cos(s-spins[j])
    return E

