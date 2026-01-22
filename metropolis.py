import numpy as np
import random as random
from enerxias import E_spin

def metropolis(spins, ady, k, T, J):
    N=int(np.sqrt(len(spins)))
    #posicion do spin seleccionado
    posicion = np.random.randint(0, len(spins))
        
    s = spins[posicion] #valor do spin seleccionado
    Es = E_spin(posicion, spins, ady, J) #enerxía debido ó spin seleccionado
    sn = random.choice(k) #valor novo do spin

    spins[posicion]=sn 
    Esn = E_spin(posicion, spins, ady, J)
    
    deltaE = Esn-Es #variación da enerxía

    if deltaE<0:
        return spins
    elif np.exp(-deltaE/T)>random.random():
        return spins
    else:
        spins[posicion]=s        
        return spins








