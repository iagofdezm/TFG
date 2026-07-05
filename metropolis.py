import numpy as np

class Metropolis:
    def __init__(self, rede, T):
        self.rede = rede
        self.T = T
        self.beta = 1.0 / T

    def paso(self):
        """Un intento de actualización en un sitio aleatorio."""
        idx = self.rede.posicion_aleatoria()
        spin_vello = self.rede.spins[idx]

        # Elegir un nuevo estado distinto
        q = self.rede.q
        spin_novo = np.random.randint(0, q)
        while spin_novo == spin_vello:
            spin_novo = np.random.randint(0, q)

        # Energía antes y después
        E_vella = self.rede.enerxia_local(idx)

        # Probar el cambio
        self.rede.spins[idx] = spin_novo
        E_nova = self.rede.enerxia_local(idx)

        delta_E = E_nova - E_vella

        # Regla de aceptación
        if delta_E > 0 and np.random.rand() >= np.exp(-self.beta * delta_E):
            # Rechazar: volver al estado anterior
            self.rede.spins[idx] = spin_vello

    def barrido(self):
        """Un barrido completo: N intentos."""
        for _ in range(self.rede.N):
            self.paso()
