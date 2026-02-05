import numpy as np
import random as random
from enerxias import E_spin
from enerxias import enerxia_total
from metropolis import metropolis
from lectura_datos import ler_spins, ler_adx
from lectura_datos import gardar_spins
from configuracion_inicial import N, k, J

'''
spins=ler_spins('configuracion_actual')
adx=ler_adx('adx')
'''

def simular(T):
    vm = [] #vector con magnetización para distinto t
    t = [] #vector con pasos temporais
    gspins = [] #vector coas configuracións do sistema

    pasos = 1000 #pasos de simulación
    g=10 #distancia entre valores de m
    for i in range(pasos*N*N):
        spins=metropolis(spins, adx, k, T, J)

        if i%(g*N*N)==0:
            gspins.append(spins)
            t.append(i)
            print(i/(g*N*N))
    vm=np.array(vm)/(N*N)
    t=np.array(t)/t[-1]
    np.savetxt(f"magnetizacion_{T}.csv", vm, delimiter=",")
    gardar_spins(gspins, 'spins_{T}.csv')
    np.savetxt(f"tempo_{T}.csv", t, delimiter=",")
    return None


