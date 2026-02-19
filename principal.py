from simulacion import equilibrar, simular
from lectura_datos import ler_spins, ler_adx
import numpy as np
import os


temperaturas=np.linspace(0.002, 3, 50)
temperaturas = np.round(temperaturas, 4)

ruta = os.path.join('datos', 'q2')

ruta_adx = os.path.join(ruta, 'adx.npz')
adx = ler_adx(ruta_adx)

for T in temperaturas:
    '''
    #Equilibrar
    ruta_spins = os.path.join(ruta, f'configuracion_inicial.npy')
    spins=np.load(ruta_spins)
    equilibrar(T, spins, adx, ruta)

    print(f'Equilibración de T={T} rematada')
    '''

    
    #Simular
    ruta_spins = os.path.join(ruta, f'T={T}', f'configuracion_equilibrada_{T}.npy')
    spins=np.load(ruta_spins)
    simular(T, spins, adx, ruta)
    
    print(f'Simulación rematada para T={T}')
    
#Gardado das temperaturas
arquivo_temperaturas = os.path.join(ruta, 'temperaturas.npy')
np.savetxt(arquivo_temperaturas, temperaturas)



