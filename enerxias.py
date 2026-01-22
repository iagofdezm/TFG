import numpy as np

def enerxia_total(spins, ady, J):
    #Inicializamos o contador de enerxia
    E=0
    for i in range(len(spins)):
        s = spins[i]
        E = E - J*s*(np.sum(ady[i]))
    return E/2.0

def E_spin(posicion, spins, ady, J):
    #A posición será o índice no vector 1D
    s = spins[posicion]
    E = -J*s*(np.sum(ady[posicion]))
    return E

