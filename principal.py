import numpy as np
import random as random
from enerxias import E_spin
from enerxias import enerxia_total
from metropolis import metropolis
from lectura_datos import ler_spins, ler_adx
from lectura_datos import gardar_spins
from configuracion_inicial import N, k, J


spins=ler_spins('configuracion_actual.npz')
adx=ler_adx('adx.npz')


def simular(T, spins, adx):
    t = [] #vector con pasos temporais
    gspins = [] #vector coas configuracións do sistema

    pasos = 10000 #pasos de simulación
    g=10 #distancia entre valores de m
    for i in range(pasos*N*N):
        spins=metropolis(spins, adx, k, T, J)

        if i%(g*N*N)==0:
            gspins.append(spins.copy())
            t.append(i)
            print(i/(g*N*N))
    t=np.array(t)/t[-1]
    gardar_spins(gspins, f'spins_{T:.1f}.npz')
    np.savetxt(f"tempo_{T:.1f}.npz", t, delimiter=",")
    return None

temperaturas=np.linspace(0.00001, 3, 20)

for T in temperaturas:
    simular(T, spins, adx)
    print('Simulación rematada')


