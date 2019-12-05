import numpy as np
from enum import Enum
import math


class Seed:
    def __init__(self, s=43):
        self.seed = (2 * s) - 1

    def getSeed(self):
        return self.seed

    def setSeed(self, ns):
        self.seed = ns

class GeradorVariavelAleatoria:
    def __init__(self,  seed: Seed, a=143.0, m=519.0):
        self.a = a
        self.m = m
        self.seed=seed

    def gerar(self):
        self.seed.setSeed((self.a * self.seed.getSeed()) % self.m)
        return self.seed.getSeed()/self.m

class DistribuicaoExponencial:
    def __init__(self):
        self.seed = Seed()
        self.gerador_va = GeradorVariavelAleatoria(self.seed)
    
    def gerar(self):
        return float(-(0.1/math.log(1 - self.gerador_va.gerar())))

class DistribuicaoNormal:
    def __init__(self):
        self.seed = Seed()
        self.a = 0
        self.b = 1
        self.gerador_va = GeradorVariavelAleatoria(self.seed)
    
    def gerar(self):
        return self.a + (self.b-self.a)* self.gerador_va.gerar()



exp = DistribuicaoExponencial()
normal = DistribuicaoNormal()
class Distribuicoes(Enum):
    NORMAL = {'name': 'Normal', 'func': normal.gerar}
    EXPONENCIAL= {'name': 'Exponencial', 'func': exp.gerar}
    POISSON = {'name': 'Poisson', 'func': np.random.poisson}
    BINOMIAL = {'name': 'Binomial', 'func': np.random.binomial}

