import numpy as np

def enerxia_total(rede):
    """Energía total del sistema."""
    E = 0
    spins = rede.spins
    J = rede.J

    for i in range(rede.N):
        s = spins[i]
        for vec in rede.veciños[i]:
            if spins[vec] == s:
                E -= J
    # Cada enlace se cuenta dos veces → dividir entre 2
    return E / 2

def enerxia_por_spin(rede):
    return enerxia_total(rede) / rede.N

def magnetizacion_por_spin(rede):
    spins = rede.spins
    q = rede.q
    N = rede.N

    angulos = 2*np.pi * spins / q
    mx = np.sum(np.cos(angulos)) / N
    my = np.sum(np.sin(angulos)) / N

    return np.sqrt(mx**2 + my**2)


def susceptibilidad_magnetica(magnetizaciones, T, N):
    """Calcula la susceptibilidad magnética por spin.

    Parámetros:
    - magnetizaciones: array de magnetización por spin para cada muestra.
    - T: temperatura.
    - N: número total de espines en la red.

    Retorna la susceptibilidad magnética por spin usando:
        chi = beta * N * (⟨m^2⟩ - ⟨m⟩^2)
    donde m es la magnetización por spin de cada muestra.
    """
    mags = np.asarray(magnetizaciones, dtype=float)
    if T <= 0:
        raise ValueError("La temperatura T debe ser mayor que cero.")

    beta = 1.0 / T
    var_m = np.mean(mags**2) - np.mean(mags)**2
    return beta * N * var_m

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