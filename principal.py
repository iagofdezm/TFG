from simulacion import equilibrar, simular
from lectura_datos import ler_spins, ler_adx
import numpy as np

adx=ler_adx('adx.npz')

temperaturas=np.linspace(0.001, 3, 5)

for T in temperaturas:
    spins=ler_spins('configuracion_inicial.npz')
    equilibrar(T, spins, adx, 'datos\\q2')
    print(f'Simulación rematada para T={T:.1f}')


