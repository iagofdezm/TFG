import numpy as np
import matplotlib.pyplot as plt
from lectura_datos import ler_adx, ler_spins
from enerxias import magnetizacion


spins = ler_spins('configuracion_actual.npz')
adx = ler_adx('adx.npz')

m = magnetizacion(spins, adx, J=1)
print(m)


