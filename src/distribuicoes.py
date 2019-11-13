import numpy as np
from enum import Enum

class Distribuicoes(Enum):
    NORMAL = {'name': 'Normal', 'func': np.random.normal}
    EXPONENCIAL= {'name': 'Exponencial', 'func': np.random.exponential}
    POISSON = {'name': 'Poisson', 'func': np.random.poisson}
    BINOMIAL = {'name': 'Binomial', 'func': np.random.binomial}