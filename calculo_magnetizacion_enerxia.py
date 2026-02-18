import numpy as np
import os
from lectura_datos import ler_adx
from enerxias import magnetizacion, enerxia_total
from principal import temperaturas


adx = ler_adx('adx.npz')
ruta = os.path.join('datos', 'q2')

vm= []
vm2 = []
ve = []
ve2 = []

for T in temperaturas:

    ruta1 = os.path.join(ruta, f'T={T}', 'simulacion.npy')
    simulacion = np.load(ruta)

    mpro = 0
    m2pro = 0
    epro = 0
    e2pro = 0

    for i in range(len(simulacion)):
        m = magnetizacion(simulacion[i], adx, J=1)
        m = m[2]
        mpro = mpro + m
        m2 = m*m
        m2pro = m2pro + m2
        e = enerxia_total(simulacion[i], adx, J=1)
        epro = epro + e
        e2 = e2 + e*e
        e2pro = e2pro + e2
    
    mpro = mpro/len(simulacion)
    m2pro = m2pro/len(simulacion)
    epro = epro/len(simulacion)
    e2pro = e2pro/len(simulacion)

    vm.append(mpro)
    vm2.append(m2pro)
    ve.append(epro)
    ve2.append(e2pro)

vm = np.array(vm)
vm2 = np.array(vm2)
ve = np.array(ve)
ve2 = np.array(ve2)

#Gardado dos vectores de magnetizacións e enerxías
rutavm = os.path.join(ruta, 'vm.csv')
np.savetxt(rutavm, vm)
rutavm2 = os.path.join(ruta, 'vm2.csv')
np.savetxt(rutavm2, vm2)
rutave = os.path.join(ruta, 've.csv')
np.savetxt(rutave, ve)
rutave2 = os.path.join(ruta, 've2.csv')
np.savetxt(rutave2, ve2)




