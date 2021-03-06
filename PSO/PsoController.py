# ------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#
# ------------------------------------------------------------------------------+

# --- IMPORT DEPENDENCIES ------------------------------------------------------+

import numpy as np
from random import randint

class ParticulaController:

    def atualizaPosicao(self, particula):
        '''
        Esta função é responsável pela movimentação das partículas no espaço, calculando suas respectivas velocidades
        para descobrir as novas posições.

        - A variáveis c é constante para o cálculo, convencionalmente utiliza-se 2.5
        - e1 e e2 são variáveis de atrito para o movimento da partícula
        - valorMaximo é um limite que não permite a ser ultrapassada, convencionalmente utiliza-se [-6, 6]
        '''
        c = 1.49618
        w = 0.7298

        e1 = np.random.rand()
        e2 = np.random.rand()
        valorMaximo = 6
        for i, velocidade in enumerate(particula._velocidade):
            velocidade = (velocidade*w) + c * e1 * (particula._melhorPosicaoLocal[i] - particula._posicao[i]) + c * e2 * (particula._melhorPosicaoGlobal[i] - particula._posicao[i])

            if abs(velocidade) > valorMaximo and abs(velocidade) is velocidade:
                velocidade = valorMaximo
            elif abs(velocidade) > valorMaximo:
                velocidade = -valorMaximo
            velocidade = self.sigmoid(velocidade)

            if np.random.rand(1) < velocidade:
                particula._posicao[i] = 1
            else:
                particula._posicao[i] = 0

            particula._velocidade[i] = velocidade

    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-(x)))


class EnxameController:

    pc = None

    def __init__(self):
        self.pc = ParticulaController()

    def atualizaEnxame(self, enxame):
        for particula in enxame._particulas:
            self.pc.atualizaPosicao(particula)
