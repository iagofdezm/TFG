import numpy as np
import random as random
from enerxias import E_spin
from enerxias import enerxia_total
from metropolis import metropolis
from lectura_datos import ler_rede
from lectura_datos import gardar_rede
from configuracion_inicial import N, k, J

spins, ady = ler_rede('configuracion_inicial.npz')

def simular(T):
    vm = [] #vector con magnetización para distinto t
    t = [] #vector con pasos temporais
    gspins = [] #vector coas configuracións do sistema

    #m=0 contador de magnetización
    pasos = 1000 #pasos de simulación
    g=10 #distancia entre valores de m
    for i in range(pasos*N*N):
        spins=metropolis(spins, ady, k, T, J)

        if i%(g*N*N)==0:

            m=np.sum(spins)
            vm.append(m)
            gspins.append(spins)
            t.append(i)
            print(i/(g*N*N))
    vm=np.array(vm)/(N*N)
    t=np.array(t)/t[-1]
    np.savetxt("t3.csv", vm, delimiter=",")
    np.savetxt('spins.csv', gspins, delimeter=',')
    np.savetxt("tempo.csv", t, delimiter=",")
    return None