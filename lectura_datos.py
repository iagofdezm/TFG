import numpy as np
#Lectura de datos
def ler_rede(nome_arquivo):
    datos = np.load(nome_arquivo, allow_pickle=True)
    spins = datos["spins"]
    ady = datos["ady"].tolist()
    return spins, ady

#Gardado da configuración da rede nun arquivo binario
def gardar_rede(spins, ady, nome_arquivo): 
    ady_obj = np.array(ady, dtype=object)
    return np.savez(nome_arquivo, spins=spins, ady=ady_obj, allow_pickle=True)
