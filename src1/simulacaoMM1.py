import numpy as np
import pandas as pd
from mm1 import *

class SimulacaoMM1:
    def __init__(self, chegada, atendimento, distribuicao = 'Exponencial'):
        self.chegada = chegada
        self.atendimento = atendimento
        self.distribuicao = distribuicao
        self.mm1 = MM1(None, self.chegada, self.atendimento)
        self.mm1.calcularTudo()

    def gerarDistribuicaoNumpy(self, parametro = 1):
        # Retorna uma variável da distribuição selecionada
        if self.distribuicao == 'Exponencial':
            return np.random.exponential(1/parametro)

        elif self.distribuicao == 'Normal':
            return abs(np.random.normal())

        elif self.distribuicao == 'Uniforme':
            return abs(np.random.uniform())

        else:
            raise Exception('Distribuição não reconhecida/disponibilizada')
    
    def gerarSimulacaoMM1(self):
        while True:
            self.simulacaoMM1 = self.gerarTabelaSimulacaoMM1()
            if abs(self.simulacaoMM1['TClS'].mean() - self.mm1.l) < 0.5: break

    def gerarTabelaSimulacaoMM1(self):
        # M/M/1
        i = 1
        tcr = 0
        tsr = 0

        # TCR/TSR: tempo chegada/saída no relógio, TF: tempo de fila, TAO: tempo atendente ocioso
        # TClS: tempo cliente no sistema
        data = {'ID': [], 'TEC': [], 'TCR': [], 'TES': [], 'TF':[], 'TSR': [], 'TClS': [], 'TAO': []}

        #while i <= 1000:
        while tcr <= 1:
            tec = self.gerarDistribuicaoNumpy(self.chegada)
            tes = self.gerarDistribuicaoNumpy(self.atendimento)
            tcr = tcr + tec

            tf = max(0, tsr - tcr)
            tao = max(0, tcr - tsr)

            if tcr < tsr: tsr = tsr + tes + tf
            else: tsr = tcr + tes

            tcls = tf + tes

            data['ID'].append(i)
            data['TEC'].append(tec)
            data['TES'].append(tes)
            data['TCR'].append(tcr)
            data['TSR'].append(tsr)
            data['TF'].append(tf)
            data['TAO'].append(tao)
            data['TClS'].append(tcls)

            i = i + 1

        return pd.DataFrame(data)

    def gerarTabelaComparacao(self):
        data = {
            'TIPO': ['Simulação M/M/1', 'Modelo M/M/1'],
            'W': [self.simulacaoMM1['TClS'].mean(), self.mm1.l],
            'Wq': [self.simulacaoMM1['TF'].mean(), self.mm1.wq],
            'Ws': [self.simulacaoMM1['TClS'].mean() - self.simulacaoMM1['TF'].mean(), self.mm1.ws],
            'L': [None, self.mm1.l],
            'Lq': [None, self.mm1.lq],
            'Ls': [None, self.mm1.ls]
        }

        return pd.DataFrame(data)

    def mostrarComparacao(self):
        return self.gerarTabelaComparacao()

    def mostrarSimulacao(self):
        self.gerarSimulacaoMM1()
        return self.simulacaoMM1