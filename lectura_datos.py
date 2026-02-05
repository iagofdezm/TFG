import numpy as np
#Lectura de datos
def ler_spins(nome_arquivo): 
    datos = np.load(nome_arquivo) 
    spins = datos["spins"] 
    return spins

def ler_adx(nome_arquivo):
    datos = np.load(nome_arquivo, allow_pickle=True)
    adx = datos['adx'].tolist()
    return adx



#Gardado da configuración da rede nun arquivo binario
def gardar_adx(adx, nome_arquivo): 
    adx_obj = np.array(adx, dtype=object)
    return np.savez(nome_arquivo, adx=adx_obj, allow_pickle=True)

#Gardado do microestado actual de spins
def gardar_spins(spins, nome_arquivo):
    return np.savez(nome_arquivo, spins=spins)
