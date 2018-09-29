# ------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   08, 2018
#
# ------------------------------------------------------------------------------+

# from Controller import *
from PSO.PsoController import EnxameController

class PsoLearning:

    ec = None

    def __init__(self):
        self.ec = EnxameController()

    def aprendizagem(self, enxame):
        # print("Aprendizagem PSO")
        self.ec.atualizaEnxame(enxame)
