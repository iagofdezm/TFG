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


def magnetizacion(spins, adx, J=1):
    N2 = len(spins)
    mx = np.sum(np.cos(spins))/N2
    my = np.sum(np.sin(spins))/N2
    mtotal = np.sqrt(mx**2+my**2)
    return mx, my, mtotal
