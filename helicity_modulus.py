import numpy as np
from rede import Rede


def helicity_modulus(rede, T):
    '''
    Cálculo do helicity modulus ao longo da dirección x
    '''
    spins = rede.spins
    N = rede.N
    q = rede.q
    J = rede.J
    vec = rede.veciños

    #Ángulos
    thetas = 2 * np.pi * spins / q

    #Sumatorios
    cos_sum = 0.0
    sen_sum = 0.0

    for i in range(N):
        #Obtención do índice do veciño da dereita
        #Só consideramos o veciño da dereita para non contar dúas veces o mesmo enlace
        j = vec[i][3] 

        delta_theta = thetas[i] - thetas[j]

        cos_sum = cos_sum + np.cos(delta_theta)
        sen_sum = sen_sum + np.sin(delta_theta)

    a = cos_sum * J / N
    b = sen_sum * J * J / (T * N)

    return a - b



