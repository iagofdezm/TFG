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
    '''
    enerxias = [] #vector coas enerxías
    magnetizacions = [] #vector coas magnetizacións
    '''
    pasos = 5000 #pasos de simulación
    g=20 #distancia entre valores de m
    for i in range(pasos*N*N):
        spins=metropolis(spins, adx, k, T, J)
        
        if i%(g*N*N)==0:
            
            #Enfriamento
            T = max(T_final, 0.97*T)
            '''
            #Cálculo e gardado da magnetización
            m = magnetizacion(spins, adx, J=1)
            magnetizacions.append(m)
            #Cálculo e gardado da enerxía
            enerxia = enerxia_total(spins, adx, J=1)
            enerxias.append(enerxia)
            '''

            print(i/(g*N*N), '/', pasos)
    '''
    archivom = f"magnetizacion_{T:.3f}.npz"
    rutam = os.path.join(q, archivom)

    archivoe = f"enerxia_{T:.3f}.npz"
    rutae = os.path.join(q, archivoe)
    

    np.savetxt(rutam, magnetizacions, delimiter=",")
    np.savetxt(rutae, enerxias, delimiter=",")
    '''
    archivos = f'configuracion_equilibrada_{T:.4f}.npz'
    rutas = os.path.join(q, archivos)

    gardar_spins(spins, rutas)
    return None


def simular(T, spins, adx):
    mprom = 0
    m2prom = 0
    eprom = 0
    e2prom = 0
    pasos = 10000 #pasos de simulación
    g=20 #distancia entre valores de m
    for i in range(pasos*N*N):
        spins=metropolis(spins, adx, k, T, J)

        if i%(g*N*N)==0:
            e = enerxia_total(spins, adx, J=1)
            eprom = eprom + e
            e2prom = e2prom + e*e
            m = magnetizacion(spins, adx, J=1)
            mprom = mprom + m
            m2prom = m2prom + m*m
            print(i/(g*N*N))
    return eprom/(pasos/g), e2prom/(pasos/g), mprom/(pasos/g), m2prom/(pasos/g)