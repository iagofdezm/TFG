from simulacion import equilibrar, simular
from lectura_datos import ler_spins, ler_adx
import numpy as np

adx=ler_adx('datos\\q2\\adx.npz')

temperaturas=np.linspace(0.001, 3, 50)

eprom = []
e2prom = []
mprom = []
m2prom = []

for T in temperaturas:
    spins=ler_spins(f'datos\\q2\\configuracion_equilibrada_{T:.4f}.npz')
    v = simular(T, spins, adx)
    eprom.append(v[0])
    e2prom.append(v[1])
    mprom.append(v[2])
    m2prom.append(v[3])
    print(f'Simulación rematada para T={T:.1f}')

g=20
pasos=5000
#t = np.linspace(0, pasos, int(pasos/g))
#np.savetxt('datos\\q2\\tempo', t, delimeter=',')
np.savetxt('datos\\q2\\temperaturas', temperaturas)
