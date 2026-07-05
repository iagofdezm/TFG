import numpy as np

class Rede:
    def __init__(self, L, q, J=1.0, seed=None):
        self.L = L
        self.q = q
        self.J = J
        self.N = L * L

        if seed is not None:
            np.random.seed(seed)

        # Spins en 1D
        self.spins = np.random.randint(0, q, size=self.N)

        # Matriz de adyacencia
        self.veciños = self.definicion_veciños()

    def definicion_veciños(self):
        N = self.N
        L = self.L
        vec = [[] for _ in range(N)]

        for i in range(L):
            for j in range(L):
                idx = i * L + j

                arriba    = ((i - 1) % L) * L + j
                abaixo  = ((i + 1) % L) * L + j
                esquerda  = i * L + (j - 1) % L
                dereita = i * L + (j + 1) % L

                vec[idx] = [arriba, abaixo, esquerda, dereita]

        return vec

    
    def enerxia_local(self, idx):
        s = self.spins[idx]
        E = 0
        for v in self.veciños[idx]:
            diff = (s - self.spins[v]) * (2*np.pi / self.q)
            E -= self.J * np.cos(diff)
        return E

    def posicion_aleatoria(self):
        return np.random.randint(0, self.N)
