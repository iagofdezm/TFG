import numpy as np
#Lectura de datos
def ler_spins(nome_arquivo): 
    datos = np.load(nome_arquivo) 
    spins = datos["spins"] 
    return spins

def ler_adyacencia(nome_arquivo):
    datos = np.load(nome_arquivo, allow_pickle=True)
    ady = datos['ady'].tolist()
    return ady



#Gardado da configuración da rede nun arquivo binario
def gardar_ady(ady, nome_arquivo): 
    ady_obj = np.array(ady, dtype=object)
    return np.savez(nome_arquivo, ady=ady_obj, allow_pickle=True)

#Gardado do microestado actual de spins
def gardar_spins(spins, nome_arquivo):
    return np.savez(nome_arquivo, spins=spins)
