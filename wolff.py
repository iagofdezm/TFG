import numpy as np
import random as random


def wolff(spins, adx, T, J=1):

    N = len(spins)

    #Elección do eixo de reflexión
    phi = random.random()*2*np.pi
    n = np.array([np.cos(phi), np.sin(phi)])

    #Elección do spin inicial
    semente = random.randrange(N)

    # Repflexión do spin respecto do eixo
    def reflex(theta):
        return (2*phi - theta)%(2*np.pi)

    #Proxección do spin sobre o eixo de reflexión
    def prox(theta):
        return np.cos(theta)*n[0]+np.sin(theta)*n[1]

    # Inicialización do clúster
    cluster = {semente}
    stack = [semente] #spins candidatos a unirse ó clúster

    #Creación do clúster
    while stack:
        i = stack.pop()
        si_prox = prox(spins[i])

        for j in adx[i]:
            if j not in cluster:
                sj_prox = prox(spins[j])

                # Probabilidade de engadir o spin ó clúster
                p = 1-np.exp(-2 *J*si_prox*sj_prox/T)

                if random.random() < p:
                    cluster.add(j)
                    stack.append(j)

    #Reflexión dos spins do clúster
    for i in cluster:
        spins[i] = reflex(spins[i])

    return spins