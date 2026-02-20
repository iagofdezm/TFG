import numpy as np
import os
from lectura_datos import ler_adx
from enerxias import magnetizacion, enerxia_total

N = 50
ruta = os.path.join('datos', 'q2')

ruta_adx = os.path.join(ruta, 'adx.npz')
adx = ler_adx(ruta_adx)

ruta_temperaturas = os.path.join(ruta, 'temperaturas.npy')
temperaturas = np.loadtxt(ruta_temperaturas)

vm= []
vm2 = []
ve = []
ve2 = []

for T in temperaturas:

    ruta1 = os.path.join(ruta, f'T={T}', 'simulacion.npy')
    simulacion = np.load(ruta1)

    mpro = 0
    m2pro = 0
    epro = 0
    e2pro = 0

    for i in range(len(simulacion)):
        mag = magnetizacion(simulacion[i], adx, J=1)
        m = mag[2]
        mpro = mpro + m
        m2 = m*m
        m2pro = m2pro + m2
        e = enerxia_total(simulacion[i], adx, J=1)
        epro = epro + e
        e2 = e*e
        e2pro = e2pro + e2

    l = len(simulacion)
    mpro = mpro/l
    m2pro = m2pro/l
    epro = epro/l
    e2pro = e2pro/l

    vm.append(mpro)
    vm2.append(m2pro)
    ve.append(epro)
    ve2.append(e2pro)

    print(f'Cálculos rematados para T={T}')

vm = np.array(vm)
vm2 = np.array(vm2)
ve = np.array(ve)
ve2 = np.array(ve2)

#Cálculo da suceptibilidade
susceptibilidade = N*(vm2-vm*vm)/temperaturas

#Gardado dos vectores das magnitudes calculadas
rutavm = os.path.join(ruta, 'vm.csv')
np.savetxt(rutavm, vm)
rutavm2 = os.path.join(ruta, 'vm2.csv')
np.savetxt(rutavm2, vm2)
rutave = os.path.join(ruta, 've.csv')
np.savetxt(rutave, ve)
rutave2 = os.path.join(ruta, 've2.csv')
np.savetxt(rutave2, ve2)
rutasusceptibilidade = os.path.join(ruta, 'susceptibilidade.csv')
np.savetxt(rutasusceptibilidade, susceptibilidade)




