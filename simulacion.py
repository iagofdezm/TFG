import numpy as np
import os
import random as random
from metropolis import metropolis
from wolff import wolff
from configuracion_inicial import N, k, J
from enerxias import magnetizacion, enerxia_total

def equilibrar(T_final, spins, adx, ruta):
    T = 4 #Temperatura inicial
    
    enerxias = [] #vector coas enerxías
    magnetizacions = [] #vector coas magnetizacións
    
    pasos = 5000 #pasos de simulación
    g=20 #distancia entre valores de m
    for i in range(pasos*N*N):
        #spins=metropolis(spins, adx, k, T, J)
        spins=wolff(spins, adx, T)
        
        
        if i%(g*N*N)==0:
            
            #Enfriamento
            T = max(T_final, 0.97*T)
            
            #Cálculo e gardado da magnetización
            m = magnetizacion(spins, adx, J=1)
            m = m[2]
            magnetizacions.append(m)
            #Cálculo e gardado da enerxía
            enerxia = enerxia_total(spins, adx, J=1)
            enerxias.append(enerxia)
            

            print(i/(g*N*N), '/', pasos/g)
    
    
    # Crea a carpeta para simular á T dada
    carpeta = os.path.join(ruta, f'T={T}')
    os.makedirs(carpeta, exist_ok=True) 


    arquivom = f"magnetizacion_equilibracion_{T}.npy"
    rutam =  os.path.join(carpeta, arquivom)

    arquivoe = f"enerxia_equilibracion_{T}.npy"
    rutae = os.path.join(carpeta, arquivoe)
    
    #Gardado da evolución da magnetización e da enerxía
    np.save(rutam, magnetizacions)
    np.save(rutae, enerxias)
    
    #Gardado da configuración equilibrada
    arquivos = f'configuracion_equilibrada_{T}.npy'
    rutas = os.path.join(ruta, f'T={T}', arquivos)

    np.save(rutas, spins)
    return None


def simular(T, spins, adx, ruta):
    pasos = 10000 #pasos de simulación
    g = 20 #pasos de distancia entre configuraciones guardadas
    gspins = []
    for i in range(pasos*N*N):
        #spins=metropolis(spins, adx, k, T, J)
        spins=wolff(spins, adx, T, J=1)

        if i%(g*N*N)==0:
            gspins.append(spins)
            print(i/(g*N*N), '/', pasos/g)

    gspins = np.array(gspins)
    rutasim = os.path.join(ruta, f'T={T}', 'simulacion.npy')
    np.save(rutasim, gspins)
    return None





