import numpy as np

def enerxia_total(spins, ady, J):
    #Inicializamos o contador de enerxia
    E=0
    for i in range(len(spins)):
        s = spins[i]
        vec = ady[i] #Posición dos veciños
        svec=0 #Contador do spin dos veciños
        for j in vec:
            svec=svec+spins[j]
        E = E - J*s*svec
    return E/2.0

def E_spin(posicion, spins, ady, J):
    #A posición será o índice no vector 1D
    s = spins[posicion]
    vec = ady[posicion] #Posición dos veciños
    svec=0 #Contador do spin dos veciños
    for j in vec:
        svec=svec+spins[j]
    E = -J*s*svec
    return E

