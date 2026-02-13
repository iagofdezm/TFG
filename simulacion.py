import numpy as np
import os
import random as random
from enerxias import enerxia_total, magnetizacion
from metropolis import metropolis
from lectura_datos import ler_spins, ler_adx
from lectura_datos import gardar_spins
from configuracion_inicial import N, k, J

def equilibrar(T_final, spins, adx, q):
    T = 4
    t = [] #vector con pasos temporais

    enerxias = [] #vector coas enerxías
    magnetizacions = [] #vector coas magnetizacións

    pasos = 10000 #pasos de simulación
    g=20 #distancia entre valores de m
    for i in range(pasos*N*N):
        spins=metropolis(spins, adx, k, T, J)

        if i%(g*N*N)==0:
            #Enfriamento
            T = max(T_final, 0.99*T)
            #Cálculo e gardado da magnetización
            m = magnetizacion(spins, adx, J=1)
            magnetizacions.append(m)
            #Cálculo e gardado da enerxía
            enerxia = enerxia_total(spins, adx, J=1)
            enerxias.append(enerxia)

            t.append(i)
            print(i/(g*N*N), '/', pasos)
    t=np.array(t)/t[-1]
    
    archivom = f"magnetizacion_{T:.1f}.npz"
    rutam = os.path.join(q, archivom)

    archivoe = f"enerxia_{T:.1f}.npz"
    rutae = os.path.join(q, archivoe)
    
    archivot = f"tempo_{T:.1f}.npz"
    rutat = os.path.join(q, archivot)

    np.savetxt(rutam, magnetizacions, delimiter=",")
    np.savetxt(rutae, enerxias, delimiter=",")
    np.savetxt(rutat, t, delimiter=",")

    archivos = f'configuracion_equlibrada_{T:.1f}.npz'
    rutas = os.path.join(q, archivos)

    gardar_spins(spins, rutas)
    return None


def simular(T, spins, adx):
    t = [] #vector con pasos temporais
    gspins = [] #vector coas configuracións do sistema

    pasos = 1000 #pasos de simulación
    g=20 #distancia entre valores de m
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